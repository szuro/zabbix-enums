from enum import IntEnum


class DiscoveryFlag(IntEnum):
    PLAIN = 0
    DISCOVERED = 4


class EntityStatus(IntEnum):
    ENABLED = 0
    DISABLED = 1
