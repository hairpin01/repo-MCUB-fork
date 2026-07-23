from typing import Any
from core.lib.types import Kernel

class OpenAgentPlugin:
    """Base class for OpenAgent plugins."""
    name: str = ""
    version: str = "0.1.0"
    author: str = ""
    description: str = ""
    tool_registry: tuple[str, ...] = ()
    tool_map: dict[str, str] = {}
    tool_docs: dict[str, dict[str, str]] = {}
    dangerous_tools: set[str] = set()
    config_defaults: dict[str, object] = {}

    def __init__(self, agent: "OpenAgent") -> None:
        self._agent = agent
        self.kernel: Kernel = self._agent.kernel
        self.client = self._agent.client

    @property
    def agent(self) -> "OpenAgent":
        return self._agent

    def add_runtime_comment(self, runtime_token: str | None, comment: str) -> bool:
        """Queue a live comment for the current OpenAgent run."""
        return self._agent.add_runtime_comment(runtime_token, comment)

    def create_background_tool_task(
        self,
        *,
        tool_name: str,
        attrs_raw: str = "",
        body: str = "",
        source_event: Any | None = None,
        status_event: Any | None = None,
        runtime_token: str | None = None,
        label: str = "",
    ) -> str:
        """Run an OpenAgent tool in background and comment when it finishes."""
        return self._agent.create_background_tool_task(
            tool_name=tool_name,
            attrs_raw=attrs_raw,
            body=body,
            source_event=source_event,
            status_event=status_event,
            runtime_token=runtime_token,
            label=label,
        )

    async def on_load(self) -> None:
        """Called after plugin is registered."""
        pass

__all__ = [
    'OpenAgentPlugin'
]
