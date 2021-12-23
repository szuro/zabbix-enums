from enum import IntEnum


class EventSeverity(IntEnum):
    NOT_CLASSIFIED = 0
    INFORMATION = 1
    WARNING = 2
    AVERAGE = 3
    HIGH = 4
    DISASTER = 5


class EventSuppressed(IntEnum):
    NO = 0
    YES = 1


class EventObjectTrigger(IntEnum):
    TRIGGER = 0


class EventObjectInternal(IntEnum):
    TRIGGER = 0
    ITEM = 4
    LLD = 5


class EventSource(IntEnum):
    TRIGGER = 0
    DISCOVERY = 1
    AUTOREGISTRATION = 2
    INTERNAL = 3


class EventObjectDiscovery(IntEnum):
    HOST = 1
    SERVICE = 2


class EventObjectAutoregistration(IntEnum):
    HOST = 3
