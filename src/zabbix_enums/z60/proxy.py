"""https://www.zabbix.com/documentation/6.0/en/manual/api/reference/proxy/object"""
from zabbix_enums import _ZabbixEnum


class ProxyStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.0/en/manual/api/reference/proxy/object#proxy

    Type of proxy.
    """
    ACTIVE = 5
    PASSIVE = 6


class ProxyTLSConnect(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.0/en/manual/api/reference/proxy/object#proxy

    Connections to host.
    """
    NO_ENCRYPTION = 1
    PSK = 2
    CERTIFICATE = 4


class HostTLSAccept(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.0/en/manual/api/reference/proxy/object#proxy

    Connections from host.
    Possible bitmap values.
    """
    NO_ENCRYPTION = 1
    PSK = 2
    CERTIFICATE = 4


class ProxyAutoCompress(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.0/en/manual/api/reference/proxy/object#proxy

    [Readonly]
    Indicates if communication between Zabbix server and proxy is compressed.
    """
    NO = 0
    YES = 1


class ProxyInterfaceUseIp(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.0/en/manual/api/reference/proxy/object#proxy-interface

    Whether the connection should be made via IP address.
    """
    NO = 0
    YES = 1
