from zabbix_enums.common import _ZabbixEnum


class ProblemSeverity(_ZabbixEnum):
    NOT_CLASSIFIED = 0
    INFORMATION = 1
    WARNING = 2
    AVERAGE = 3
    HIGH = 4
    DISASTER = 5


class ProblemSuppressed(_ZabbixEnum):
    NO = 0
    YES = 1


class ProblemObjectTrigger(_ZabbixEnum):
    TRIGGER = 0


class ProblemObjectInternal(_ZabbixEnum):
    TRIGGER = 0
    ITEM = 4
    LLD = 5


class ProblemAcknowledged(_ZabbixEnum):
    NO = 0
    YES = 1


class ProblemSource(_ZabbixEnum):
    TRIGGER = 0
    INTERNAL = 3
