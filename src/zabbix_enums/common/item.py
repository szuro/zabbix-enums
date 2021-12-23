from enum import IntEnum


class ItemFlag(IntEnum):
    PLAIN = 0
    DISCOVERED = 4


class ItemStatus(IntEnum):
    ENABLED = 0
    DISABLED = 1


class ItemValueType(IntEnum):
    NUMERIC_FLOAT = 0
    CHARACTER = 1
    LOG = 2
    NUMERIC_UNSIGNED = 3
    TEXT = 4


class ItemState(IntEnum):
    NORMAL = 0
    NOT_SUPPORTED = 1


class ItemAuthTypeSSH(IntEnum):
    PASSWORD = 0
    PUBLIC_KEY = 1
