"""https://www.zabbix.com/documentation/current/en/manual/api/reference/hanode/object"""
from zabbix_enums import _ZabbixEnum


class HighAvailabilityNodeStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/current/en/manual/api/reference/hanode/object#high-availability-node

    State of the node.
    """
    STANDBY = 0
    STOPPED_MANUALLY = 1
    UNAVAILABLE = 2
    ACTIVE = 3
