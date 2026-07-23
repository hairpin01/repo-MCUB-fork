from dataclasses import dataclass, field

@dataclass
class OASession:
    """Single named conversation thread within a Telegram chat."""
    id: str
    name: str
    chat_id: int
    created_at: float
    updated_at: float
    messages: list[dict[str, str]] = field(default_factory=list)
    model: str | None = None
    thinking_notes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "chat_id": self.chat_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "messages": [dict(item) for item in self.messages if isinstance(item, dict)],
            "model": self.model,
            "thinking_notes": list(self.thinking_notes),
        }

    @classmethod
    def from_dict(cls, d: dict) -> "OASession":
        return cls(
            id=str(d.get("id", "")),
            name=str(d.get("name", "New chat")),
            chat_id=int(d.get("chat_id", 0)),
            created_at=float(d.get("created_at", 0)),
            updated_at=float(d.get("updated_at", 0)),
            messages=list(d.get("messages") or []),
            model=str(d.get("model") or "") or None,
            thinking_notes=[str(item) for item in (d.get("thinking_notes") or []) if str(item).strip()],
        )

__all__ = [
    'OASession'
]
