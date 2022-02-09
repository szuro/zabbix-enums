from enum import IntEnum


class TriggerFlag(IntEnum):
    PLAIN = 0
    DISCOVERED = 4


class TriggerStatus(IntEnum):
    ENABLED = 0
    DISABLED = 1


class TriggerPriority(IntEnum):
    NOT_CLASSIFIED = 0
    INFORMATION = 1
    WARNING = 2
    AVERAGE = 3
    HIGH = 4
    DISASTER = 5


class TriggerState(IntEnum):
    NORMAL = 0
    UNKNOWN = 1


class TriggerType(IntEnum):
    GENERATE_SINGLE_EVENT = 0
    NOT_GENERATE_MULTIPLE_EVENTS = 0
    GENERATE_MULTIPLE_EVENTS = 1


class TriggerValue(IntEnum):
    OK = 0
    PROBLEM = 1


class TriggerRecoveryMode(IntEnum):
    EXPRESSION = 0
    RECOVERY_EXPRESSION = 1
    NONE = 2


class TriggerCorrelationMode(IntEnum):
    ALL_PROBLEMS = 0
    TAG_VALUES_MATCH = 1


class TriggerManualClose(IntEnum):
    NO = 0
    YES = 1
