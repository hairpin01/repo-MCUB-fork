# 🥞🥞🥞🥞🥞🥞🥞🥞🥞🥞🥞
# powered by MCUB userbot
# 🥞🥞🥞🥞🥞🥞🥞🥞🥞🥞🥞

import core.lib.loader.module_base as loader # БЛИНОВЫЙ ИМПОРТ
from core.lib.types import Event # 🥞🥞🥞

class BlinMod(loader.ModuleBase):
  name: str = "блинMod" # БЛИНЫ
  description: str = "блины?"
  version: str = "6766676676"

  @loader.watcher(out=True) # 🥞🥞🥞🥞🥞🥞🥞🥞
  async def watcher_blin(self, message: Event) -> None: # БЛИНОВАЯ ФУНКЦИЯ
    text: str = message.raw_text
    if text is None or text.startswith(str(self.get_prefix())):
      return
      
    blin_text: str = text.replace("блин", "🥞") # ОДААА 🥞ы ОБОЖАЮ 🥞!!!!!!!!!!!!
    if blin_text == text:
      return
      
    await self.edit(
      message,
      blin_text
    ) # редачим 🥞овый текст

