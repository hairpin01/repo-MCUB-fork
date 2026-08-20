# SPDX-License-Identifier: MIT
"""Telegram media v2 surface; workspace file operations migrate in Task 13."""
from ._telegram_v2 import build_plugin

MANIFEST, HANDLERS = build_plugin("file", include=("file.send", "file.download_media"))
PLUGIN_MANIFEST = MANIFEST
TOOL_HANDLERS = HANDLERS
DEFERRED_WORKSPACE_TOOL_IDS = ("file.read_text", "file.write", "file.edit", "file.patch")
