from . import _ZabbixEnum, _Priority, _Suppressed, _ObjectTrigger, _ObjectInternal, _ObjectSource


EventSeverity = _Priority
EventSuppressed = _Suppressed
EventObjectTrigger = _ObjectTrigger
EventObjectInternal = _ObjectInternal
EventSource = _ObjectSource


class EventObjectDiscovery(_ZabbixEnum):
    HOST = 1
    SERVICE = 2


class EventObjectAutoregistration(_ZabbixEnum):
    HOST = 3
