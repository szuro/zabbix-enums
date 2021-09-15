from enum import IntEnum
from ._common import Priority, Suppressed, ObjectTrigger, ObjectInternal


EventSeverity = Priority
EventSuppressed = Suppressed
EventObjectTrigger = ObjectTrigger
EventObjectInternal = ObjectInternal


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
