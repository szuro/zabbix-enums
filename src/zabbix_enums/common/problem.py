from enum import IntEnum
from . import _Priority, _Suppressed, _ObjectTrigger, _ObjectInternal


ProblemSeverity = _Priority
ProblemSuppressed = _Suppressed
ProblemObjectTrigger = _ObjectTrigger
ProblemObjectInternal = _ObjectInternal


class ProblemAcknowledged(IntEnum):
    NO = 0
    YES = 1


class ProblemSource(IntEnum):
    TRIGGER = 0
    INTERNAL = 3
