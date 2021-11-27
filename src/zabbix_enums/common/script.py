from enum import IntEnum


class ScriptExecuteOn(IntEnum):
    AGENT = 0
    SERVER = 1
    SERVER_PROXY = 2


class ScriptHostAccess(IntEnum):
    READ = 2
    WRITE = 3
