import subprocess
import asyncio
import shlex
import html
from typing import Any

import core.lib.loader.module_base as loader
from core.lib.types import (
  InlineMessage,
  Event,
)
from core.lib.loader.module_config import (
  ModuleConfig,
  ConfigValue,
  String,
  Boolean,
)
import utils

SU = "su -c"

class RootTermux(loader.ModuleBase):
  name = "TermuxRoot"

  strings: utils.Strings | dict = {
    "name": "null"
  } 

  config = ModuleConfig(
    ConfigValue(
      "path_args",
      SU,
      description="Путь до бинарника su, или команда (нужно указать в PATH)",
      validator=String(),
    ),
    ConfigValue(
      "delete_quote",
      False,
      description="нужно когда используешь sudo или что-то ещё необычное",
      validator=Boolean()
    )
  )

  async def run(self, cmd: str, timeout: int = 30) -> tuple[int, str]:
    """
      cmd - str
      timeount - int - default: 30
      return tuple[code: int, output: str].
    """
    proc = await asyncio.create_subprocess_shell(
        f'{self.config.get("path_args", SU)} {shlex.quote(cmd) if not self.config.get("delete_quote", False) else cmd}',
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.STDOUT,
    )
    try:
        out, _ = await asyncio.wait_for(proc.communicate(), timeout)
    except asyncio.TimeoutError:
        proc.kill()
        await proc.wait()
        return 124, "<timeout>"
    return proc.returncode, out.decode(errors="replace")

  @loader.callback()
  async def cb_close(self, call: InlineMessage, data=None) -> None:
    try:
      await self.client.delete_messages(call.chat_id, [call.message.id])
    except Exception:
      await call.edit_rich("🫥")
      return
    try:
      await call.edit_rich("🫥")
    except Exception:
      pass
      
  async def _build_command(self, cmd: str, button=None) -> tuple[Any, str]:
    code, out = await self.run(cmd)
    if not out:
      out = "<No output>"

    modules = [
      [
        "<h1>Exec SU command</h1>",
      ],
      [
        f'<pre><code class="language-shell">Cmd: {html.escape(cmd.strip())}</code></pre>',
      ],
      [
        f"<pre><code>\n{html.escape(out.strip())}</code></pre>",
      ],
      [
        f"<p><b>exit code:</b> <code>{code}</code></p>",
      ],
    ]
    buttons = []
    if button is not None:
      buttons.append([button]) # потом чёт сделаю

    buttons.append([
      self.Button.inline(
        self.strings("buttons")("close"), # словарь buttons из langpack
        self.cb_close,
      )
    ])

    return buttons, "\n".join(" ".join(sublist) for sublist in modules)

  @loader.command("su", doc_ru="exec command")
  async def cmd_tsu(self, message: Event) -> None:
    cmd = self.args_raw(message)
    if not cmd:
      await self.edit(
        message,
        f"usage: {self.get_prefix()}su [command]"
      )
      return
      
    buttons, text = await self._build_command(cmd)

    await self.subinline.rich_form(
      message,
      text,
      buttons=buttons,
    )

  

  