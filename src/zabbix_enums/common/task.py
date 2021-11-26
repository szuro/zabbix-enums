from enum import IntEnum


class TaskType(IntEnum):
    DIAGNOSTIC = 1
    CHECK_NOW = 6

class TaskStatus(IntEnum):
    NEW = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    EXPIRED = 4

class TaskStatisticResult(IntEnum):
    ERROR = -1
    CREATED = 0
