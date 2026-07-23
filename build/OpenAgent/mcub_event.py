from typing import Any
import asyncio

class _MCUBEvent:
    def __init__(self, outer: "OpenAgent", source_event: Any, text: str) -> None:
        self._outer = outer
        self._source_event = source_event
        self.text = text
        self.raw_text = text
        self.message = self
        self.client = outer.client
        self.chat_id = outer._event_chat_id(source_event)
        self.sender_id = getattr(outer.kernel, "ADMIN_ID", None) or getattr(
            source_event, "sender_id", None
        )
        self.id = getattr(source_event, "id", 0)
        self.out = True
        self.piped = True
        self.pipe_input = None
        self.pipe_output = None
        self.pipe_exit_code = 0
        self.no_add_args_to_input = False
        self._outputs: list[str] = []

    async def edit(
        self, text: str, *args: Any, **kwargs: Any
    ) -> "OpenAgent._MCUBEvent":
        await asyncio.sleep(0)
        self._outputs.append(str(text))
        return self

    async def reply(
        self, text: str, *args: Any, **kwargs: Any
    ) -> "OpenAgent._MCUBEvent":
        await asyncio.sleep(0)
        self._outputs.append(str(text))
        return self

    async def respond(
        self, text: str, *args: Any, **kwargs: Any
    ) -> "OpenAgent._MCUBEvent":
        await asyncio.sleep(0)
        self._outputs.append(str(text))
        return self

    async def delete(self, *args: Any, **kwargs: Any) -> None:
        await asyncio.sleep(0)
        return None

    async def get_reply_message(self) -> Any:
        if hasattr(self._source_event, "get_reply_message"):
            return await self._source_event.get_reply_message()
        return None

    async def get_chat(self) -> Any:
        if hasattr(self._source_event, "get_chat"):
            return await self._source_event.get_chat()
        return None

    async def get_sender(self) -> Any:
        if hasattr(self._source_event, "get_sender"):
            return await self._source_event.get_sender()
        return None

    @property
    def output(self) -> str:
        return "\n\n".join(self._outputs).strip()

__all__ = [
    '_MCUBEvent'
]
