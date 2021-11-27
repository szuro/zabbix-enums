from enum import IntEnum


class ScriptType(IntEnum):
    SCRIPT = 0
    IPMI = 1
    SSH = 2
    TELNET = 3
    WEBHOOK = 5


class ScriptScope(IntEnum):
    ACTION = 1
    MANUAL_HOST = 2
    MANUAL_EVENT = 4
