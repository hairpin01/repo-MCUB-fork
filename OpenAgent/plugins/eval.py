# SPDX-License-Identifier: MIT
"""Bounded expression evaluation with no runtime or host object access."""
from __future__ import annotations

import ast
import json
import math
import time
from typing import Any, Callable, Mapping

from OpenAgentLib.PluginSDK import CapabilityClient, PluginManifest, PluginToolDeclaration
from OpenAgentLib.ToolCompatibility import TOOL_COMPATIBILITY_MATRIX
from OpenAgentLib.ToolKernel import ToolCall


_MAX_CODE_LENGTH = 4_096
_MAX_AST_NODES = 256
_MAX_AST_DEPTH = 20
_MAX_STEPS = 1_000
_MAX_RESULT_BYTES = 8_192
_MAX_TIMEOUT_MS = 100
_INPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "code": {"type": "string"},
        "variables": {"type": "object"},
        "timeout_ms": {"type": "integer"},
    },
    "required": ["code"],
    "additionalProperties": False,
}
_JSON_VALUE_SCHEMA = {"type": "object", "properties": {"json": {"type": "string"}}, "required": ["json"], "additionalProperties": False}
_OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {"ok": {"type": "boolean"}, "value": _JSON_VALUE_SCHEMA, "steps": {"type": "integer"}},
    "required": ["ok", "value", "steps"],
    "additionalProperties": False,
}


def _declaration() -> PluginToolDeclaration:
    entry = next(item for item in TOOL_COMPATIBILITY_MATRIX if item.canonical_id == "eval.python")
    return PluginToolDeclaration(
        entry.canonical_id, aliases=entry.aliases, input_schema=_INPUT_SCHEMA, output_schema=_OUTPUT_SCHEMA,
        capabilities=frozenset({entry.capability_class}), description="Evaluate one bounded JSON expression locally.",
        confirmation=entry.confirmation_class, concurrency=entry.concurrency_class,
        idempotency=entry.idempotency_class, migration_disposition=entry.migration_disposition,
    )


def _json_value(value: Any, name: str = "value") -> Any:
    try:
        encoded = json.dumps(value, ensure_ascii=True, separators=(",", ":"), allow_nan=False)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name} must be JSON-compatible") from exc
    if len(encoded.encode("utf-8")) > _MAX_RESULT_BYTES:
        raise ValueError(f"{name} exceeds the result limit")
    return value


def _check_tree(tree: ast.AST) -> None:
    nodes = list(ast.walk(tree))
    if len(nodes) > _MAX_AST_NODES:
        raise ValueError("expression has too many AST nodes")

    def depth(node: ast.AST, value: int = 0) -> int:
        if value > _MAX_AST_DEPTH:
            raise ValueError("expression AST is too deep")
        return max((depth(child, value + 1) for child in ast.iter_child_nodes(node)), default=value)

    depth(tree)


def _evaluate(code: Any, variables: Any, timeout_ms: Any) -> tuple[Any, int]:
    if not isinstance(code, str) or not code or len(code) > _MAX_CODE_LENGTH:
        raise ValueError("code must be bounded non-empty text")
    if not isinstance(variables, Mapping):
        raise ValueError("variables must be a JSON object")
    values = {key: _json_value(value, "variable") for key, value in variables.items() if isinstance(key, str)}
    if len(values) != len(variables) or any("__" in key for key in values):
        raise ValueError("variables require non-dunder string names")
    if not isinstance(timeout_ms, int) or isinstance(timeout_ms, bool) or not 1 <= timeout_ms <= _MAX_TIMEOUT_MS:
        raise ValueError("timeout_ms is outside the allowed range")
    try:
        tree = ast.parse(code, mode="eval")
    except SyntaxError as exc:
        raise ValueError("only one expression is accepted") from exc
    _check_tree(tree)
    state = {"steps": 0, "deadline": time.monotonic() + timeout_ms / 1000, "cpu": time.process_time(), "timeout": timeout_ms / 1000}

    def step() -> None:
        state["steps"] += 1
        if state["steps"] > _MAX_STEPS or time.monotonic() > state["deadline"] or time.process_time() - state["cpu"] > state["timeout"]:
            raise ValueError("expression exceeded its execution limit")

    def evaluate(node: ast.AST) -> Any:
        step()
        if isinstance(node, ast.Constant):
            if node.value is None or isinstance(node.value, (bool, int, float, str)):
                if isinstance(node.value, float) and not math.isfinite(node.value):
                    raise ValueError("non-finite numbers are not allowed")
                return node.value
        elif isinstance(node, ast.Name):
            if "__" not in node.id and node.id in values:
                return values[node.id]
            raise ValueError("unknown or unsafe name")
        elif isinstance(node, ast.List):
            return [evaluate(item) for item in node.elts]
        elif isinstance(node, ast.Tuple):
            return [evaluate(item) for item in node.elts]
        elif isinstance(node, ast.Dict):
            result: dict[str, Any] = {}
            for key, value in zip(node.keys, node.values, strict=True):
                key_value = evaluate(key) if key is not None else None
                if not isinstance(key_value, str):
                    raise ValueError("dictionary keys must be strings")
                result[key_value] = evaluate(value)
            return result
        elif isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.Not, ast.UAdd, ast.USub)):
            value = evaluate(node.operand)
            if isinstance(node.op, ast.Not):
                return not value
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                raise ValueError("unary arithmetic requires a number")
            return +value if isinstance(node.op, ast.UAdd) else -value
        elif isinstance(node, ast.BoolOp) and isinstance(node.op, (ast.And, ast.Or)):
            result = evaluate(node.values[0])
            for item in node.values[1:]:
                if bool(result) != isinstance(node.op, ast.And):
                    break
                result = evaluate(item)
            return result
        elif isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.FloorDiv, ast.Mod, ast.Pow)):
            left, right = evaluate(node.left), evaluate(node.right)
            if isinstance(node.op, ast.Pow) and (not isinstance(right, int) or isinstance(right, bool) or abs(right) > 12):
                raise ValueError("power exponent is outside the allowed range")
            if isinstance(node.op, ast.Mult) and isinstance(right, int) and isinstance(left, (str, list)) and len(left) * abs(right) > _MAX_RESULT_BYTES:
                raise ValueError("sequence multiplication exceeds the result limit")
            operators: Mapping[type[ast.operator], Callable[[Any, Any], Any]] = {
                ast.Add: lambda a, b: a + b, ast.Sub: lambda a, b: a - b, ast.Mult: lambda a, b: a * b,
                ast.Div: lambda a, b: a / b, ast.FloorDiv: lambda a, b: a // b, ast.Mod: lambda a, b: a % b,
                ast.Pow: lambda a, b: a ** b,
            }
            return operators[type(node.op)](left, right)
        elif isinstance(node, ast.Compare):
            left = evaluate(node.left)
            operators: Mapping[type[ast.cmpop], Callable[[Any, Any], bool]] = {
                ast.Eq: lambda a, b: a == b, ast.NotEq: lambda a, b: a != b, ast.Lt: lambda a, b: a < b,
                ast.LtE: lambda a, b: a <= b, ast.Gt: lambda a, b: a > b, ast.GtE: lambda a, b: a >= b,
                ast.In: lambda a, b: a in b, ast.NotIn: lambda a, b: a not in b,
            }
            for operation, comparator in zip(node.ops, node.comparators, strict=True):
                if type(operation) not in operators or not operators[type(operation)](left, evaluate(comparator)):
                    return False
                left = evaluate(comparator)
            return True
        elif isinstance(node, ast.IfExp):
            return evaluate(node.body if evaluate(node.test) else node.orelse)
        elif isinstance(node, ast.Subscript):
            target, index = evaluate(node.value), evaluate(node.slice)
            if not isinstance(target, (str, list, dict)) or not isinstance(index, (int, str)) or isinstance(index, bool):
                raise ValueError("unsupported subscript")
            return target[index]
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and "__" not in node.func.id and not node.keywords:
            arguments = [evaluate(argument) for argument in node.args]
            functions: Mapping[str, Callable[..., Any]] = {"abs": abs, "bool": bool, "int": int, "len": len, "max": max, "min": min, "str": str, "sum": sum}
            function = functions.get(node.func.id)
            if function is not None:
                return function(*arguments)
        raise ValueError("expression uses a forbidden syntax node")

    value = _json_value(evaluate(tree.body), "result")
    return value, state["steps"]


def _run(call: ToolCall, _capability: CapabilityClient) -> Mapping[str, Any]:
    value, steps = _evaluate(call.arguments["code"], call.arguments.get("variables", {}), call.arguments.get("timeout_ms", 25))
    return {"ok": True, "value": {"json": json.dumps(value, ensure_ascii=True, separators=(",", ":"), allow_nan=False)}, "steps": steps}


_TOOLS = (_declaration(),)
MANIFEST = PluginManifest("openagent.eval", "2.0.0", "2", "plugins.eval.HANDLERS", _TOOLS, frozenset({"sandbox-local"}))
HANDLERS: Mapping[str, Callable[[ToolCall, CapabilityClient], Mapping[str, Any]]] = {"eval.python": _run}
PLUGIN_MANIFEST = MANIFEST
TOOL_HANDLERS = HANDLERS
