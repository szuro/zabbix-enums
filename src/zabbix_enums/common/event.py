from enum import IntEnum
from .._common import Priority, Suppressed, ObjectTrigger, ObjectInternal, ObjectSource


EventSeverity = Priority
EventSuppressed = Suppressed
EventObjectTrigger = ObjectTrigger
EventObjectInternal = ObjectInternal
EventSource = ObjectSource


class EventObjectDiscovery(IntEnum):
    HOST = 1
    SERVICE = 2


class EventObjectAutoregistration(IntEnum):
    HOST = 3
