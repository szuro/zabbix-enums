from . import _DiscoveryFlag, _EntityStatus, _Priority, _ZabbixEnum


TriggerFlag = _DiscoveryFlag
TriggerStatus = _EntityStatus
TriggerPriority = _Priority


class TriggerState(_ZabbixEnum):
    NORMAL = 0
    UNKNOWN = 1


class TriggerType(_ZabbixEnum):
    GENERATE_SINGLE_EVENT = 0
    NOT_GENERATE_MULTIPLE_EVENTS = 0
    GENERATE_MULTIPLE_EVENTS = 1


class TriggerValue(_ZabbixEnum):
    OK = 0
    PROBLEM = 1


class TriggerRecoveryMode(_ZabbixEnum):
    EXPRESSION = 0
    RECOVERY_EXPRESSION = 1
    NONE = 2


class TriggerCorrelationMode(_ZabbixEnum):
    ALL_PROBLEMS = 0
    TAG_VALUES_MATCH = 1


class TriggerManualClose(_ZabbixEnum):
    NO = 0
    YES = 1
