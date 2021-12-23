from enum import IntEnum
from . import _Priority


ProblemSeverity = _Priority


class ProblemSuppressed(IntEnum):
    NO = 0
    YES = 1


class ProblemObjectTrigger(IntEnum):
    TRIGGER = 0


class ProblemObjectInternal(IntEnum):
    TRIGGER = 0
    ITEM = 4
    LLD = 5


class ProblemAcknowledged(IntEnum):
    NO = 0
    YES = 1


class ProblemSource(IntEnum):
    TRIGGER = 0
    INTERNAL = 3
