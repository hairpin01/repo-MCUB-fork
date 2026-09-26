# SPDX-License-Identifier: MIT
# scop: kernel min v1.4.7.1
# or XPatchKernel. enable ExtraProxy for module and scopes: Kernel

import core.lib.loader.module_base as loader
from core.lib.utils.exceptions import CallInsecure

aliases_pack = {
    "gs": "t git status",
    "ga": "t git add ",
    "gaa": "t git add -A",
    "gc": "t git commit -m ",
    "gca": "t git commit --amend -m ",
    "gp": "t git push",
    "gpl": "t git pull",
    "gcl": "t git clone ",
    "gb": "t git branch",
    "gch": "t git checkout ",
    "gcb": "t git checkout -b ",
    "gl": "t git log --oneline --graph --decorate -20",
    "gd": "t git diff",
    "gds": "t git diff --staged",
    "gr": "t git restore ",
    "grs": "t git restore --staged ",
    "grh": "t git reset --hard HEAD",
    "gst": "t git stash",
    "gstp": "t git stash pop",
    "grm": "t git remote -v",
    "gfe": "t git fetch --all --prune",
    "dps": "t docker ps",
    "dpsa": "t docker ps -a",
    "di": "t docker images",
    "drun": "t docker run -it --rm ",
    "dex": "t docker exec -it ",
    "dlogs": "t docker logs -f ",
    "dstop": "t docker stop ",
    "dstart": "t docker start ",
    "drm": "t docker rm ",
    "drmi": "t docker rmi ",
    "dpull": "t docker pull ",
    "dpush": "t docker push ",
    "dbuild": "t docker build -t ",
    "dcomp": "t docker compose ",
    "dcup": "t docker compose up -d",
    "dcdown": "t docker compose down",
    "dcps": "t docker compose ps",
    "dclogs": "t docker compose logs -f",
    "dprune": "t docker system prune -af",
    "dvol": "t docker volume ls",
    "dnet": "t docker network ls",
    "ff": "t fastfetch",
    "ffa": "t fastfetch --show-errors",
    "ffc": "t fastfetch --config ",
    "ffj": "t fastfetch --format json",
    "ffs": "t fastfetch --structure ",
    "ffl": "t fastfetch --list-configs",
    "fflogo": "t fastfetch --logo ",
}


class AliasesTerminalPack(loader.ModuleBase):
    name = "PackAliasesTerminal"
    description = "Алиасы для терминала: git, docker, fastfetch"

    async def on_load(self) -> None:
        try:
            test_alias = getattr(self.kernel, "aliases")
        except CallInsecure as e:
            await self.kernel.handle_error(
                e,
                message=f"Please update kernel to v1.4.7.1, or added module '{self.name}' in ExtraProxy (XKernel)",
            )
            return

        for alias, command in aliases_pack.items():
            self.kernel.aliases[alias] = command
        self.kernel.config["aliases"] = self.kernel.aliases
        self.kernel.save_config()
        self.log.info("added aliases pack")
