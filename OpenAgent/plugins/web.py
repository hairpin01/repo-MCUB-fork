# SPDX-License-Identifier: MIT
"""Public web tools backed solely by the parent HTTPS capability."""
from __future__ import annotations

import html
import re
from typing import Any, Callable, Mapping
from urllib.parse import quote

from OpenAgentLib.PluginSDK import CapabilityClient, PluginManifest
from OpenAgentLib.ToolKernel import ToolCall

from ._resource_v2 import bounded_text, declaration, required_text, response_data


_TIMEOUT_SECONDS = 20
_MAX_FETCH_BYTES = 262_144
_MAX_TEXT_BYTES = 12_000
_MAX_LINKS = 100
_URL_SCHEMA = {
    "type": "object",
    "properties": {"url": {"type": "string"}},
    "required": ["url"],
    "additionalProperties": False,
}
_SEARCH_SCHEMA = {
    "type": "object",
    "properties": {"query": {"type": "string"}},
    "required": ["query"],
    "additionalProperties": False,
}
_FETCH_OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "ok": {"type": "boolean"}, "url": {"type": "string"}, "content_type": {"type": "string"},
        "content": {"type": "string"}, "truncated": {"type": "boolean"},
    },
    "required": ["ok", "url", "content_type", "content", "truncated"],
    "additionalProperties": False,
}
_LINK_OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "ok": {"type": "boolean"}, "url": {"type": "string"},
        "links": {"type": "array", "items": {"type": "string"}}, "truncated": {"type": "boolean"},
    },
    "required": ["ok", "url", "links", "truncated"],
    "additionalProperties": False,
}
_SEARCH_OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "ok": {"type": "boolean"}, "url": {"type": "string"},
        "results": {"type": "array", "items": {"type": "string"}}, "truncated": {"type": "boolean"},
    },
    "required": ["ok", "url", "results", "truncated"],
    "additionalProperties": False,
}


def _url(value: Any) -> str:
    if not isinstance(value, str) or not value or len(value) > 2_048 or "\x00" in value:
        raise ValueError("url must be bounded non-empty text")
    if not value.startswith("https://"):
        raise ValueError("only HTTPS URLs are supported")
    return value


def _fetch(capability: CapabilityClient, call: ToolCall, url: str, request_suffix: str) -> tuple[str, str, str, bool]:
    data = response_data(capability.fetch(
        url,
        f"{call.call_id}:{request_suffix}",
        timeout_seconds=_TIMEOUT_SECONDS,
        max_bytes=_MAX_FETCH_BYTES,
    ))
    content = required_text(data, "content")
    content, truncated = bounded_text(content, _MAX_TEXT_BYTES)
    final_url = data.get("url", url)
    content_type = data.get("content_type", "")
    if not isinstance(final_url, str) or not isinstance(content_type, str):
        raise ValueError("HTTPS response metadata must be strings")
    return final_url, content_type, content, bool(data.get("truncated", False) or truncated)


def _html_to_text(value: str) -> str:
    value = re.sub(r"<script\b[^>]*>.*?</script>", " ", value, flags=re.IGNORECASE | re.DOTALL)
    value = re.sub(r"<style\b[^>]*>.*?</style>", " ", value, flags=re.IGNORECASE | re.DOTALL)
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def _fetch_url(call: ToolCall, capability: CapabilityClient) -> Mapping[str, Any]:
    url, content_type, content, truncated = _fetch(capability, call, _url(call.arguments["url"]), "web.fetch-url")
    return {"ok": True, "url": url, "content_type": content_type, "content": content, "truncated": truncated}


def _read_html(call: ToolCall, capability: CapabilityClient) -> Mapping[str, Any]:
    url, content_type, content, truncated = _fetch(capability, call, _url(call.arguments["url"]), "web.read-html")
    text, text_truncated = bounded_text(_html_to_text(content), _MAX_TEXT_BYTES)
    return {"ok": True, "url": url, "content_type": content_type, "content": text, "truncated": truncated or text_truncated}


def _extract_links(call: ToolCall, capability: CapabilityClient) -> Mapping[str, Any]:
    url, _content_type, content, truncated = _fetch(capability, call, _url(call.arguments["url"]), "web.extract-links")
    links = [html.unescape(link).strip() for link in re.findall(r"\bhref\s*=\s*['\"]([^'\"]+)['\"]", content, flags=re.IGNORECASE)]
    links = [link for link in links if link][: _MAX_LINKS]
    return {"ok": True, "url": url, "links": links, "truncated": truncated or len(links) == _MAX_LINKS}


def _summarize_page(call: ToolCall, capability: CapabilityClient) -> Mapping[str, Any]:
    url, content_type, content, truncated = _fetch(capability, call, _url(call.arguments["url"]), "web.summarize")
    text, text_truncated = bounded_text(_html_to_text(content), _MAX_TEXT_BYTES)
    return {"ok": True, "url": url, "content_type": content_type, "content": text, "truncated": truncated or text_truncated}


def _search(call: ToolCall, capability: CapabilityClient) -> Mapping[str, Any]:
    query = call.arguments["query"]
    if not isinstance(query, str) or not query or len(query) > 1_024 or "\x00" in query:
        raise ValueError("query must be bounded non-empty text")
    url = _url(query) if query.startswith("https://") else f"https://duckduckgo.com/html/?q={quote(query, safe='')}"
    final_url, _content_type, content, truncated = _fetch(capability, call, url, "web.search")
    matches = re.findall(r'<a[^>]+class=["\']result__a["\'][^>]*>(.*?)</a>', content, flags=re.IGNORECASE | re.DOTALL)
    results = [_html_to_text(match) for match in matches if _html_to_text(match)][:5]
    return {"ok": True, "url": final_url, "results": results, "truncated": truncated}


_TOOLS = (
    declaration("web.search", _SEARCH_SCHEMA, _SEARCH_OUTPUT_SCHEMA, "Search through a parent-controlled HTTPS request."),
    declaration("web.fetch_url", _URL_SCHEMA, _FETCH_OUTPUT_SCHEMA, "Fetch a public HTTPS URL through the parent broker."),
    declaration("web.read_html", _URL_SCHEMA, _FETCH_OUTPUT_SCHEMA, "Fetch and extract text through the parent broker."),
    declaration("web.extract_links", _URL_SCHEMA, _LINK_OUTPUT_SCHEMA, "Fetch and extract bounded links through the parent broker."),
    declaration("web.summarize_page", _URL_SCHEMA, _FETCH_OUTPUT_SCHEMA, "Fetch and summarize text through the parent broker."),
)
MANIFEST = PluginManifest(
    plugin_id="openagent.web",
    version="2.0.0",
    api_version="2",
    entrypoint="plugins.web.HANDLERS",
    tools=_TOOLS,
    capabilities=frozenset({capability for tool in _TOOLS for capability in tool.capabilities}),
)
HANDLERS: Mapping[str, Callable[[ToolCall, CapabilityClient], Mapping[str, Any]]] = {
    "web.search": _search,
    "web.fetch_url": _fetch_url,
    "web.read_html": _read_html,
    "web.extract_links": _extract_links,
    "web.summarize_page": _summarize_page,
}
PLUGIN_MANIFEST = MANIFEST
TOOL_HANDLERS = HANDLERS
