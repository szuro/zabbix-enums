from . import _Priority, _Suppressed, _ObjectTrigger, _ObjectInternal, _ZabbixEnum


ProblemSeverity = _Priority
ProblemSuppressed = _Suppressed
ProblemObjectTrigger = _ObjectTrigger
ProblemObjectInternal = _ObjectInternal


class ProblemAcknowledged(_ZabbixEnum):
    NO = 0
    YES = 1


class ProblemSource(_ZabbixEnum):
    TRIGGER = 0
    INTERNAL = 3
