from enum import IntEnum


class ItemPrototypeDiscover(IntEnum):
    DISCOVER = 0
    DONT_DISCOVER = 1


class ItemPrototypeStatus(IntEnum):
    ENABLED = 0
    DISABLED = 1
    UNSUPPORTED = 3
