from enum import IntEnum
from . import _DiscoveryFlag, _EntityStatus, _Priority


TriggerFlag = _DiscoveryFlag
TrigerStatus = _EntityStatus
TriggerPriority = _Priority


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
