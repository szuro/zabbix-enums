"""https://www.zabbix.com/documentation/5.0/en/manual/api/reference/hostgroup/object"""
from zabbix_enums import _ZabbixEnum


class HostGroupFlag(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/hostgroup/object#host-group
    
    [Readonly]
    Origin of the host group.
    """
    PLAIN = 0
    DISCOVERED = 4


class HostGroupInternal(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/hostgroup/object#host-group
    
    [Readonly]
    Whether the group is used internally by the system.
    An internal group cannot be deleted.
    """
    NO = 0
    YES = 1
    NOT_INTERNAL = 0
    INTERNAL = 1
