from enum import IntEnum
from . import _Priority, _ObjectTrigger, _ObjectInternal


ProblemSeverity = _Priority


class ProblemSuppressed(IntEnum):
    NO = 0
    YES = 1


ProblemObjectTrigger = _ObjectTrigger
ProblemObjectInternal = _ObjectInternal


class ProblemAcknowledged(IntEnum):
    NO = 0
    YES = 1


class ProblemSource(IntEnum):
    TRIGGER = 0
    INTERNAL = 3
