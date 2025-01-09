"""https://www.zabbix.com/documentation/current/en/manual/api/reference/sla/object"""
from zabbix_enums import _ZabbixEnum


class SLAPeriod(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/current/en/manual/api/reference/sla/object#sla

    Reporting period of the SLA.
    """
    DAILY = 0
    WEEKLY = 1
    MONTHLY = 2
    QUARTERLY = 3
    ANNUALLY = 4


class SLAStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/current/en/manual/api/reference/sla/object#sla

    Status of the SLA.
    """
    DISABLED = 0
    ENABLED = 1


class SLAServiceTagOperator(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/current/en/manual/api/reference/sla/object#sla-service-tag

    SLA service tag operator.
    """
    EQUALS = 0
    LIKE = 2
