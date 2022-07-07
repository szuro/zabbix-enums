"""https://www.zabbix.com/documentation/5.4/en/manual/api/reference/service/object"""
from zabbix_enums import _ZabbixEnum


class ServiceAlgorithm(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.4/en/manual/api/reference/service/object#service

    Algorithm used to calculate the state of the service.
    """
    DO_NOT_CALCULATE = 0
    AT_LEAST_ONE_CHILD_WITH_PROBLEM = 1
    ALL_CHILDREN_WITH_PROBLEM = 2


class ServiceShowSLA(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.4/en/manual/api/reference/service/object#service

    Whether SLA should be calculated.
    """
    DO_NOT_CALCULATE = 0
    CALCULATE = 1


class ServiceStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.4/en/manual/api/reference/service/object#service

    [Readonly]
    Whether the service is in OK or problem state.
    """
    OK = 0
    WARNING = 2
    AVERAGE = 3
    HIGH = 4
    DISASTER = 5


class ServiceTimeType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.4/en/manual/api/reference/service/object#service-time

    Service time type.
    """
    PLANNED_UPTIME = 0
    PLANNED_DOWNTIME = 1
    ONE_TIME_DOWNTIME = 2


class ServiceDependencySoft(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.4/en/manual/api/reference/service/object#service-dependency

    Type of dependency between services.
    """
    NO = 0
    YES = 1
