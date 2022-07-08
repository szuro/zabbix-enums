"""https://www.zabbix.com/documentation/5.0/en/manual/api/reference/problem/object"""
from zabbix_enums import _ZabbixEnum


class ProblemSource(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/problem/object#problem-object

    Type of the problem event.
    """
    TRIGGER = 0
    INTERNAL = 3


class ProblemObjectTrigger(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/problem/object#problem-object

    Type of object that is related to the problem event.
    Possible values for trigger events.
    """
    TRIGGER = 0


class ProblemObjectInternal(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/problem/object#problem-object

    Type of object that is related to the problem event.
    Possible values for internal events.
    """
    TRIGGER = 0
    ITEM = 4
    LLD = 5


class ProblemAcknowledged(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/problem/object#problem-object

    Acknowledge state for problem.
    """
    NO = 0
    YES = 1


class ProblemSeverity(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/problem/object#problem-object

    Problem current severity.
    """
    NOT_CLASSIFIED = 0
    INFORMATION = 1
    WARNING = 2
    AVERAGE = 3
    HIGH = 4
    DISASTER = 5


class ProblemSuppressed(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/problem/object#problem-object

    Whether the problem is suppressed.
    """
    NO = 0
    YES = 1
