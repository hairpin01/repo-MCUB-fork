# SPDX-License-Identifier: MIT
# Auto-loaded OpenAgent runtime mixins for MCUB.
# Source: https://github.com/hairpin01/repo-MCUB-fork/tree/main/lib/OpenAgent

from __future__ import annotations

from .oasession import (
    OASession
)
from .session_manager import (
    _SESSION_PREFERENCES,
    SessionManager,
    _OpenAgentSessionsMixin,
)
from .plugin import (
    OpenAgentPlugin,
    _OpenAgentPluginSkillMixin,
    _OpenAgentTelegramMediaMixin,
    _OpenAgentStatusMixin,
    _OpenAgentAgentLoopMixin,
)
from .todo import (
    OpenAgentTodoService,
    _OpenAgentTodoMixin,
    _TODO_STATUS_ALIASES,
    _DEFAULT_TODO_STATUS_MAP,
    _WHITESPACE_RE,
)
from .lifecycle import (
    _OpenAgentLifecycleMixin
)
from .placeholder import (
    _PLACEHOLDER_RE,
    OpenAgentProviderService,
    OpenAgentTemplateService,
    _OpenAgentProviderMixin,
)
from .tool import (
    _DEFAULT_TOOL_STATUS_EMOJIS,
    OpenAgentToolDisplayService,
    _OpenAgentToolDisplayMixin,
    _TOOL_GROUP_ALIASES,
    _OpenAgentRuntimeToolsMixin,
    _OpenAgentToolRegistryMixin,
)
from .context import (
    OpenAgentContextService,
    _OpenAgentContextMixin,
)
from .response import (
    _OpenAgentResponseMixin
)

OPENAGENT_LIB_VERSION = '0.8.0-main.build:1043' # fallback

__all__ = [
    'OPENAGENT_LIB_VERSION',
    '_WHITESPACE_RE',
    '_PLACEHOLDER_RE',
    '_TODO_STATUS_ALIASES',
    '_DEFAULT_TODO_STATUS_MAP',
    '_SESSION_PREFERENCES',
    '_TOOL_GROUP_ALIASES',
    '_DEFAULT_TOOL_STATUS_EMOJIS',
    'OASession',
    'SessionManager',
    'OpenAgentPlugin',
    '_OpenAgentLifecycleMixin',
    'OpenAgentProviderService',
    'OpenAgentTemplateService',
    '_OpenAgentProviderMixin',
    'OpenAgentTodoService',
    '_OpenAgentTodoMixin',
    'OpenAgentToolDisplayService',
    '_OpenAgentToolDisplayMixin',
    'OpenAgentContextService',
    '_OpenAgentContextMixin',
    '_OpenAgentSessionsMixin',
    '_OpenAgentPluginSkillMixin',
    '_OpenAgentRuntimeToolsMixin',
    '_OpenAgentTelegramMediaMixin',
    '_OpenAgentStatusMixin',
    '_OpenAgentAgentLoopMixin',
    '_OpenAgentResponseMixin',
    '_OpenAgentToolRegistryMixin',
]
