from zabbix_enums.common import _ZabbixEnum


class TriggerFlag(_ZabbixEnum):
    PLAIN = 0
    DISCOVERED = 4


class TriggerStatus(_ZabbixEnum):
    ENABLED = 0
    DISABLED = 1


class TriggerPriority(_ZabbixEnum):
    NOT_CLASSIFIED = 0
    INFORMATION = 1
    WARNING = 2
    AVERAGE = 3
    HIGH = 4
    DISASTER = 5


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
