"""https://www.zabbix.com/documentation/7.2/en/manual/api/reference/correlation/object"""
from zabbix_enums import _ZabbixEnum


class CorrelationStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.2/en/manual/api/reference/correlation/object#correlation

    Whether the correlation is enabled or disabled.
    """
    ENABLED = 0
    DISABLED = 1


class CorrelationOperationType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.2/en/manual/api/reference/correlation/object#correlation-operation

    Type of operation.
    """
    CLOSE_OLD = 0
    CLOSE_NEW = 1


class CorrelationFilterEvalType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.2/en/manual/api/reference/correlation/object#correlation-filter

    Filter condition evaluation method.
    """
    AND_OR = 0
    AND = 1
    OR = 2
    CUSTOM = 3


class CorrelationFilterConditionType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.2/en/manual/api/reference/correlation/object#correlation-filter-condition

    Type of condition.
    """
    OLD_EVENT_TAG = 0
    NEW_EVENT_TAG = 1
    NEW_EVENT_HOST_GROUP = 2
    EVENT_TAG_PAIR = 3
    OLD_EVENT_TAG_VALUE = 4
    NEW_EVENT_TAG_VALUE = 5
