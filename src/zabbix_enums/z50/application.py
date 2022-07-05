"""https://www.zabbix.com/documentation/5.0/en/manual/api/reference/application/object"""
from zabbix_enums import _ZabbixEnum


class ApplicationFlag(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/application/object#application
    
    [Readonly]
    Origin of the application.
    """
    PLAIN = 0
    DISCOVERED = 4
