"""https://www.zabbix.com/documentation/5.4/en/manual/api/reference/maintenance/object"""
from zabbix_enums import _ZabbixEnum


class MaintenanceType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.4/en/manual/api/reference/maintenance/object#maintenance

    Type of maintenance.
    """
    WITH_DATA_COLLECTION = 0
    WITHOUT_DATA_COLLECTION = 1


class MaintenanceTagsEvalType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.4/en/manual/api/reference/maintenance/object#maintenance

    Problem tag evaluation method.
    """
    AND_OR = 0
    OR = 1


class TimePeriodEvery(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.4/en/manual/api/reference/maintenance/object#time-period

    For daily and weekly periods every defines day or week intervals at which the maintenance must come into effect.
    For monthly periods every defines the week of the month when the maintenance must come into effect.
    """
    FIRST_WEEK = 1
    SECOND_WEEK = 2
    THIRD_WEEK = 3
    FOURTH_WEEK = 4
    LAST_WEEK = 5


class TimePeriodType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.4/en/manual/api/reference/maintenance/object#time-period

    Type of time period.
    """
    one_time_only = 0
    daily = 2
    weekly = 3
    monthly = 4


class ProblemTag(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.4/en/manual/api/reference/maintenance/object#problem-tag

    Condition operator.
    """
    EQUALS = 0
    CONTAINS = 2
