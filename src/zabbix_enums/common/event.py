from enum import IntEnum
from . import _Priority, _ObjectTrigger, _ObjectInternal


EventSeverity = _Priority


class EventSuppressed(IntEnum):
    NO = 0
    YES = 1


EventObjectTrigger = _ObjectTrigger
EventObjectInternal = _ObjectInternal


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
