---
name: MCUB-modules-creator
description: Create and update debug MCUB userbot modules in app-debug using the MCUB module API, class-style modules, and inline form/callback docs.
keywords:
  - мoдyль
  - мoдyли
  - module
  - modules
  - app-debug
  - modules-debug
  - ModuleBase
  - inline
  - callback
  - command
---

# MCUB Modules Creator

Use this skill when the user asks to create, edit, update, refactor, or debug an MCUB module.

## Core identity and context

- MCUB is a **Telegram userbot**: it runs on a Telegram user account via Telethon/Telethon-MCUB.
- Do **not** assume MCUB is a regular Telegram Bot API bot running only on a bot account.
- Default commands should be **userbot commands** with `@command(...)` from `core.lib.loader.module_base`.
- Use `@bot_command(...)` only when the user explicitly needs a command handled by the auxiliary bot account.
- Inline buttons/forms still involve the inline bot layer, but the module itself is for the MCUB userbot runtime.
- Never confuse MCUB modules with Hikka modules. MCUB uses `core.lib.loader.module_base` and `ModuleBase`; Hikka-style `from .. import utils, loader` and `loader.Module` are not MCUB module style.

## Required documentation sources

Before implementing or updating a module, consult the relevant local docs:

- API index: `API_DOC.md`
- Class-style modules: `doc/registration/class-style.md`
- Inline forms: `doc/inline/inline-form.md`
- Inline callbacks and permissions: `doc/inline/callbacks.md`
- If needed, also follow linked docs from `API_DOC.md` such as:
  - `doc/guides/best-practices.md`
  - `doc/guides/module-structure.md`
  - `doc/api/module-config.md`
  - `doc/api/database.md`
  - `doc/api/errors.md`

## API boundary and dependencies

- Use **only the MCUB API** for module structure, registration, commands, inline forms, callbacks, config, database, cache, lifecycle, logging, and helpers.
- Do not invent cross-framework helpers or import APIs from Hikka/Heroku userbot frameworks.
- External Python libraries are allowed only when they are genuinely needed for the module's domain and MCUB does not provide that functionality.
  - Example: a SpeedTest module may use `speedtest-cli` or another speed test library.
  - Example: HTTP API integrations may use an existing HTTP client only if the project conventions/docs allow it.
- When using an external library:
  - add it to the module metadata `dependencies` list when appropriate;
  - keep the integration isolated behind small helper methods;
  - handle missing-package/runtime errors gracefully;
  - do not replace MCUB SDK functionality with third-party libraries.

## Output location and versioning rules

All debug modules created by this skill must live under:

```text
app-debug/{module-name}/modules-debug-v{version}.py
```

Examples:

```text
app-debug/Weather/modules-debug-v1.0.0.py
app-debug/Weather/modules-debug-v1.0.1.py
```

Rules:

1. Never put generated debug modules directly into `modules_loaded/` unless the user explicitly asks.
2. When creating a new module, create the module directory if it does not exist.
3. When updating an existing module, **always create a new file with a new version**.
4. Never overwrite or delete older builds. Old files in `app-debug/{module-name}/` are build history and must be preserved.
5. If the user gives a target version, use it exactly in both:
   - file name: `modules-debug-v{version}.py`
   - class metadata: `version = "{version}"`
6. If the user does not give a version:
   - new module: use `1.0.0`
   - update: inspect existing `modules-debug-v*.py` files and increment patch version, e.g. `1.0.0` → `1.0.1`.
7. If the requested target file already exists, do not overwrite it. Pick the next patch version or ask for confirmation if the user explicitly demanded that exact version.

## Preferred module style

Prefer class-style MCUB modules based on `ModuleBase`.

Minimal skeleton:

```python
from __future__ import annotations

# Standard library
import time

# Third-party dependencies
from telethon import events

# SDK
import core.lib.loader.module_base as loader
import utils
import core.lib.loader.module_config as cfg


class ExampleModule(loader.ModuleBase):
    name = "Example"
    version = "1.0.0"
    author = "by Example, model: {AI model}, total token: {tokens}. @Example"
    description: dict[str, str] = {
        "ru": "Oпиcaниe мoдyля",
        "en": "Module description",
    }

    @loader.command("example", doc_ru="Пpимep", doc_en="Example")
    async def cmd_example(self, event: events.NewMessage.Event) -> None:
        await self.edit(event, "Example works!")
```

Author metadata rule for AI-created modules:

- When this skill creates or substantially rewrites a module with an AI model, set the class metadata `author` to this format:

```python
author = "by {module_name}, model: {ai_model}, total token: {total_tokens}. @{module_name}"
```

- Replace `{module_name}` with the actual MCUB module `name` value.
- Replace `{ai_model}` with the AI model name if known; otherwise use `unknown`.
- Replace `{total_tokens}` with the total token count if known; otherwise use `unknown`.
- Preserve explicit human author/port attribution only when the user asks to keep it; otherwise use the AI-created format above for generated debug modules.

## Import organization

Separate imports into clear groups:

```python
from __future__ import annotations

# Standard library
import asyncio
import time
from typing import Any

# Third-party dependencies
from telethon import events

# Optional external libraries, only when truly needed
import speedtest

# SDK
import core.lib.loader.module_base as loader
import utils
import core.lib.loader.module_config as cfg
```

Import rules:

- Keep standard library imports first.
- Keep third-party dependencies separate from SDK imports.
- Keep MCUB SDK imports under a `# SDK` comment.
- Prefer this MCUB SDK style for consistency:

```python
# SDK
import core.lib.loader.module_base as loader
import utils
import core.lib.loader.module_config as cfg
```

- Then reference decorators/classes through `loader`, e.g. `loader.ModuleBase`, `@loader.command`, `@loader.callback`.
- Use `cfg` only when module configuration is needed.
- Do not import Hikka SDK as `from .. import utils, loader`.

## MCUB vs Hikka module style

Correct MCUB style:

```python
# SDK
import core.lib.loader.module_base as loader
import utils


class ModulesMod(loader.ModuleBase):
    name = "modules"
    version = "1.0.0"
```

Incorrect Hikka style for this project:

```python
# SDK
from .. import utils, loader


class ModulesMod(loader.Module):
    strings = {"name": "modules"}
```

Never convert MCUB modules into Hikka modules. Never use `loader.Module` for MCUB class-style modules; use `loader.ModuleBase`.

Class-style requirements:

- Import from `core.lib.loader.module_base` / `loader` as needed:
  - `ModuleBase`
  - `command`
  - `bot_command`
  - `owner`
  - `permission`
  - `callback`
  - `watcher`
  - `loop`
  - `event`
  - `method`
  - `inline_temp`
  - lifecycle decorators such as `on_install`, `uninstall` if documented/available in the local docs.
- Use `self.client` for userbot Telethon client operations.
- Use `self.db` for persistent data.
- Use `self.cache` for temporary TTL-like data.
- Use `self.log` for logging.
- Use `self.args(event)`, `self.args_raw(event)`, and `self.args_html(event)` for command parsing when appropriate.
- Use `self.answer`, `self.edit`, or `self.reply` rather than raw `event.edit` when a robust helper is better.
- Use localized `description` and command docs (`doc_ru`, `doc_en`) when possible.
- Use `strings` for reusable user-facing text.

## Lifecycle rules

- Initialize runtime state in `on_load`, not in `__init__`.
- If overriding `on_load()` and using `@method`, call:

```python
await super().on_load()
```

- If overriding `on_unload()` and using `@uninstall`, call `await super().on_unload()`.
- If overriding `on_install()` and using `@on_install`, call `await super().on_install()`.
- Clean up long-lived resources in `on_unload`.

## Inline forms and buttons

Important: in userbot mode, interactive inline buttons generally require an inline form message.

Prefer the class-style button factory where available:

```python
buttons = [
    [self.Button.inline("OK", self.handle_ok, ttl=300)],
    [self.Button.url("GitHub", "https://github.com")],
]
await self.kernel.inline_form(event.chat_id, "Title", buttons=buttons)
```

For callbacks:

```python
# SDK
import core.lib.loader.module_base as loader


@loader.callback(ttl=300)
async def handle_ok(self, event: events.CallbackQuery.Event) -> None:
    await event.answer("OK")
```

Inline rules:

- Keep callback TTLs finite.
- Avoid manually storing raw callback data unless needed.
- Respect callback permissions: by default inline buttons may be restricted to admins/allowed users.
- For complex inline flows, consult `doc/inline/inline-form.md` and `doc/inline/callbacks.md`.

## Safety and quality checklist

Before finishing a module:

1. Confirm the file path matches `app-debug/{module-name}/modules-debug-v{version}.py`.
2. Confirm the class `name` and `version` metadata match the requested module and file version.
3. Confirm older builds in the module directory were not removed or overwritten.
4. Confirm userbot-vs-bot semantics are correct:
   - userbot commands: `@command`
   - bot-account commands only when requested: `@bot_command`
5. Confirm all imports are needed and valid for MCUB docs.
6. Confirm no secrets, tokens, API keys, session strings, phone numbers, or credentials are hardcoded.
7. Prefer async Telethon-compatible code.
8. Prefer clear Russian and English strings/docs when the user-facing module is bilingual.
9. Confirm the module uses MCUB API only, except justified external domain libraries.
10. Confirm import groups separate standard library, third-party dependencies, optional external libraries, and `# SDK` imports.
11. Confirm no Hikka-style imports/classes are present (`from .. import utils, loader`, `loader.Module`).
12. Run a syntax check for the generated file when feasible:

```bash
python -m py_compile app-debug/{module-name}/modules-debug-v{version}.py
```

13. Run the MCUB debugger against the generated file:

```bash
python -m debugger.cli app-debug/{module-name}/modules-debug-v{version}.py
```

If the `mcub-debugger` console script is installed, this is also acceptable:

```bash
mcub-debugger app-debug/{module-name}/modules-debug-v{version}.py
```

Debugger rules:

- Treat debugger errors as blockers.
- Fix warnings when they indicate real MCUB runtime issues.
- If a warning is intentionally safe for a class-style MCUB API pattern, mention it explicitly in the final response.

## Update workflow

When the user asks to update an existing MCUB module:

1. Locate existing files in `app-debug/{module-name}/`.
2. Identify the latest `modules-debug-v{version}.py`.
3. Read the latest version and understand the current behavior.
4. Create a new file with the next version. Do not edit the old file in place.
5. Carry forward existing functionality unless the user explicitly asks to remove it.
6. Add a short changelog comment near the top only if useful; do not bloat simple modules.
7. Run syntax verification when feasible.
8. Run `python -m debugger.cli app-debug/{module-name}/modules-debug-v{version}.py` and fix debugger errors before finishing.

## Creation workflow

When the user asks to create a new MCUB module:

1. Infer a clean PascalCase class name and a filesystem-safe module directory name from the request.
2. Use version `1.0.0` unless the user specifies another version.
3. Create `app-debug/{module-name}/modules-debug-v{version}.py`.
4. Implement as a class-style `ModuleBase` module.
5. Add commands with `@command`, not Bot API handlers.
6. Add inline UI only when it improves usability or the user requests buttons/forms.
7. Verify syntax.
8. Run the MCUB debugger from `debugger/` via `python -m debugger.cli app-debug/{module-name}/modules-debug-v{version}.py`.

## Do not do

- Do not treat MCUB as a regular Telegram Bot API framework.
- Do not confuse MCUB modules with Hikka modules.
- Do not use Hikka-style `from .. import utils, loader`.
- Do not inherit from `loader.Module`; use `loader.ModuleBase`.
- Do not use non-MCUB APIs for module registration/config/database/inline/lifecycle when MCUB API exists.
- Do not overwrite `modules-debug-v*.py` builds.
- Do not delete previous debug builds.
- Do not place debug builds outside `app-debug/`.
- Do not hardcode secrets or user credentials.
- Do not use blocking synchronous network calls inside async handlers unless wrapped safely or unavoidable.
- Do not invent APIs when local docs provide the correct MCUB API.
