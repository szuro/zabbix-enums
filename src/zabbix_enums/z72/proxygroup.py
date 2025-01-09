"""https://www.zabbix.com/documentation/7.2/en/manual/api/reference/proxygroup/object"""
from zabbix_enums import _ZabbixEnum


class ProxyGroupState(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.2/en/manual/api/reference/proxygroup/object#proxy-group
    
    State of the proxy group.
    """
    UNKNOWN = 0
    OFFLINE = 1
    RECOVERING = 2
    ONLINE = 3
    DEGRADING = 4
