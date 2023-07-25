"""https://www.zabbix.com/documentation/6.2/en/manual/api/reference/hostgroup/object"""
from zabbix_enums import _ZabbixEnum


class HostGroupFlag(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/hostgroup/object#host-group
    
    [Readonly]
    Origin of the host group.
    """
    PLAIN = 0
    DISCOVERED = 4
