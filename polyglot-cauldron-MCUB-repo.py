# name: polyglot-cauldron-MCUB-repo
# author: 123
# version: 1.0.0
# description: Run code in 10 languages via local interpreters

import asyncio
import os
import tempfile

from utils import escape_html, get_args_raw

RUNNERS = {
    "js": ("node", ".js", "JavaScript", "javascript", []),
    "ts": ("ts-node", ".ts", "TypeScript", "typescript", []),
    "php": ("php", ".php", "PHP", "php", []),
    "ruby": ("ruby", ".rb", "Ruby", "ruby", []),
    "lua": ("lua", ".lua", "Lua", "lua", []),
    "perl": ("perl", ".pl", "Perl", "perl", []),
    "awk": ("awk", ".awk", "Awk", "awk", ["-f"]),
    "tcl": ("tclsh", ".tcl", "Tcl", "tcl", []),
    "groovy": ("groovy", ".groovy", "Groovy", "groovy", []),
    "r": ("Rscript", ".R", "R", "r", []),
}


def register(kernel):
    language = kernel.config.get("language", "en")

    strings = {
        "ru": {
            "no_code": "Пepeдaй кoд apгyмeнтoм или oтвeть нa cooбщeниe c кoдoм.",
            "running": "Выпoлняю...",
            "success": "OK",
            "error": "Oшибкa",
            "no_output": "(нeт вывoдa)",
            "mode_usage": "Иcпoльзoвaниe: <code>{p}polybrew mode &lt;{modes}&gt;</code>",
            "mode_set": "Peжим измeнён нa: <code>{mode}</code>",
            "bad_lang": "Heизвecтный язык. Дocтyпнo: <code>{modes}</code>",
            "help": (
                "<b>Polyglot Cauldron</b>\n"
                "<code>{p}polybrew &lt;кoд&gt;</code> - выпoлнить кoд в тeкyщeм peжимe\n"
                "Oтвeть нa cooбщeниe c кoдoм кoмaндoй <code>{p}polybrew</code>\n"
                "<code>{p}polybrew mode &lt;язык&gt;</code> - пepeключить peжим\n"
                "<code>{p}polybrew run &lt;язык&gt; &lt;кoд&gt;</code> - paзoвый зaпycк\n"
                "Языки: <code>{modes}</code>"
            ),
        },
        "en": {
            "no_code": "Provide code as an argument or reply to a message with code.",
            "running": "Running...",
            "success": "OK",
            "error": "Error",
            "no_output": "(no output)",
            "mode_usage": "Usage: <code>{p}polybrew mode &lt;{modes}&gt;</code>",
            "mode_set": "Mode set to: <code>{mode}</code>",
            "bad_lang": "Unknown language. Available: <code>{modes}</code>",
            "help": (
                "<b>Polyglot Cauldron</b>\n"
                "<code>{p}polybrew &lt;code&gt;</code> - run code in current mode\n"
                "Reply to a message containing code with <code>{p}polybrew</code>\n"
                "<code>{p}polybrew mode &lt;lang&gt;</code> - switch mode\n"
                "<code>{p}polybrew run &lt;lang&gt; &lt;code&gt;</code> - one-off run\n"
                "Languages: <code>{modes}</code>"
            ),
        },
    }

    s = strings.get(language, strings["en"])
    p = kernel.custom_prefix
    timeout = 10
    module_name = "polyglot_cauldron"
    modes = "|".join(RUNNERS.keys())

    async def get_mode():
        mode = await kernel.db_get(module_name, "mode")
        return mode if mode in RUNNERS else "js"

    async def get_code(event):
        raw = get_args_raw(event)
        if raw:
            return raw
        reply = await event.get_reply_message()
        if reply and reply.text:
            return reply.text
        return None

    async def run_code(code, mode):
        runner, ext, _, _, args = RUNNERS[mode]
        with tempfile.NamedTemporaryFile(
            suffix=ext, mode="w", delete=False, encoding="utf-8"
        ) as f:
            f.write(code)
            path = f.name
        try:
            proc = await asyncio.create_subprocess_exec(
                runner,
                *args,
                path,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
            stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=timeout)
            return proc.returncode, stdout.decode(), stderr.decode()
        except FileNotFoundError:
            return -1, "", f"{runner}: not found."
        except asyncio.TimeoutError:
            proc.kill()
            return -1, "", f"Timeout ({timeout}s)"
        finally:
            os.unlink(path)

    def build_output(code, mode, returncode, stdout, stderr):
        _, _, label, lang_id, _ = RUNNERS[mode]
        status = s["success"] if returncode == 0 else s["error"]
        out = (stdout or stderr or s["no_output"]).strip()
        return (
            f"<b>{label}</b> - <b>{escape_html(status)}</b>\n"
            f'<pre language="{lang_id}">{escape_html(code[:300])}</pre>\n'
            f"<pre>{escape_html(out[:2000])}</pre>"
        )

    @kernel.register.command(
        "polybrew", alias=["poly", "cauldron"]
    )  # <code> | mode <lang> | run <lang> <code> - multi-language runner for 10 languages
    async def polybrew_handler(event):
        try:
            raw = get_args_raw(event)
            if raw:
                parts = raw.split(maxsplit=2)
                head = parts[0]

                if head == "help":
                    await event.edit(
                        s["help"].format(p=p, modes=modes), parse_mode="html"
                    )
                    return

                if head == "mode":
                    if len(parts) < 2 or parts[1] not in RUNNERS:
                        await event.edit(
                            s["mode_usage"].format(p=p, modes=modes), parse_mode="html"
                        )
                        return
                    await kernel.db_set(module_name, "mode", parts[1])
                    await event.edit(
                        s["mode_set"].format(mode=parts[1]), parse_mode="html"
                    )
                    return

                if head == "run":
                    if len(parts) < 3:
                        await event.edit(
                            s["help"].format(p=p, modes=modes), parse_mode="html"
                        )
                        return
                    mode = parts[1]
                    code = parts[2]
                    if mode not in RUNNERS:
                        await event.edit(
                            s["bad_lang"].format(modes=modes), parse_mode="html"
                        )
                        return
                    await event.edit(s["running"], parse_mode="html")
                    rc, stdout, stderr = await run_code(code, mode)
                    await event.edit(
                        build_output(code, mode, rc, stdout, stderr), parse_mode="html"
                    )
                    return

            code = await get_code(event)
            if not code:
                await event.edit(s["no_code"], parse_mode="html")
                return

            mode = await get_mode()
            await event.edit(s["running"], parse_mode="html")
            rc, stdout, stderr = await run_code(code, mode)
            await event.edit(
                build_output(code, mode, rc, stdout, stderr), parse_mode="html"
            )

        except Exception as e:
            await kernel.handle_error(
                e, source="polyglot_cauldron:polybrew_handler", event=event
            )
