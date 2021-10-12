from enum import IntEnum


class YesNo(IntEnum):
    NO = 0
    YES = 1


class DiscoveryFlag(IntEnum):
    PLAIN = 0
    DISCOVERED = 4


class EntityStatus(IntEnum):
    ENABLED = 0
    DISABLED = 1


class Permission(IntEnum):
    READ_ONLY = 2
    READ_WRITE = 3


class Priority(IntEnum):
    NOT_CLASSIFIED = 0
    INFORMATION = 1
    WARNING = 2
    AVERAGE = 3
    HIGH = 4
    DISASTER = 5


class Suppressed(IntEnum):
    NO = 0
    YES = 1


class ObjectTrigger(IntEnum):
    TRIGGER = 0


class ObjectInternal(IntEnum):
    TRIGGER = 0
    ITEM = 4
    LLD = 5
