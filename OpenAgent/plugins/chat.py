# SPDX-License-Identifier: MIT
from ._telegram_v2 import build_plugin

MANIFEST, HANDLERS = build_plugin("chat")
PLUGIN_MANIFEST = MANIFEST
TOOL_HANDLERS = HANDLERS
