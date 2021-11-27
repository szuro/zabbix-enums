from enum import IntEnum
from . import _Priority, _Suppressed, _ObjectTrigger, _ObjectInternal, _ObjectSource


EventSeverity = _Priority
EventSuppressed = _Suppressed
EventObjectTrigger = _ObjectTrigger
EventObjectInternal = _ObjectInternal
EventSource = _ObjectSource


class EventObjectDiscovery(IntEnum):
    HOST = 1
    SERVICE = 2


class EventObjectAutoregistration(IntEnum):
    HOST = 3
