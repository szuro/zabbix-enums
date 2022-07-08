"""https://www.zabbix.com/documentation/6.0/en/manual/api/reference/autoregistration/object"""
from zabbix_enums import _ZabbixEnum


class AutoregistrationTLSAccept(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.0/en/manual/api/reference/autoregistration/object#autoregistration

    Type of allowed incoming connections for autoregistration.
    """
    INSECURE = 1
    PSK = 2
    BOTH = 3
