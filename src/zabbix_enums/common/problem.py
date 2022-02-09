from enum import IntEnum


class ProblemSeverity(IntEnum):
    NOT_CLASSIFIED = 0
    INFORMATION = 1
    WARNING = 2
    AVERAGE = 3
    HIGH = 4
    DISASTER = 5


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
