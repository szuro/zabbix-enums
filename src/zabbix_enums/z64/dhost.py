"""https://www.zabbix.com/documentation/6.4/en/manual/api/reference/dhost/object"""
from zabbix_enums import _ZabbixEnum


class DiscoveredHostStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.4/en/manual/api/reference/dhost/object#discovered-host

    Whether the discovered host is up or down.
    A host is up if it has at least one active discovered service.
    """
    UP = 0
    DOWN = 1
