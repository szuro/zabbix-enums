"""https://www.zabbix.com/documentation/6.4/en/manual/api/reference/task/object"""
from zabbix_enums import _ZabbixEnum


class TaskType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.4/en/manual/api/reference/task/object#task-object

    Type of the task.
    """
    DIAGNOSTIC = 1
    REFRESH_PROXY_CONFIGURATION = 2
    CHECK_NOW = 6
    EXECUTE_NOW = 6


class TaskStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.4/en/manual/api/reference/task/object#task-object

    [Readonly]
    Status of the task.
    """
    NEW = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    EXPIRED = 4


class StatisticResult(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.4/en/manual/api/reference/task/object#statistic-result-object

    [Readonly]
    Status of the task result.
    """
    ERROR = -1
    CREATED = 0
