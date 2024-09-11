"""https://www.zabbix.com/documentation/6.4/en/manual/api/reference/dservice/object"""
from zabbix_enums import _ZabbixEnum


class DiscoveredServiceStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.4/en/manual/api/reference/dservice/object#discovered-service
    
    Status of the service.
    """
    UP = 0
    DOWN = 1
