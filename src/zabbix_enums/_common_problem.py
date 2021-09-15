from enum import IntEnum
from ._common import Priority, Suppressed, ObjectTrigger, ObjectInternal


ProblemSeverity = Priority
ProblemSuppressed = Suppressed
ProblemObjectTrigger = ObjectTrigger
ProblemObjectInternal = ObjectInternal


class ProblemAcknowledged(IntEnum):
    NO = 0
    YES = 1


class ProblemSource(IntEnum):
    TRIGGER = 0
    INTERNAL = 3
