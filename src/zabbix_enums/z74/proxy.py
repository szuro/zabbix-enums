"""https://www.zabbix.com/documentation/7.4/en/manual/api/reference/proxy/object"""
from zabbix_enums import _ZabbixEnum


class ProxyOperatingMode(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/proxy/object#proxy

    Type of proxy.
    """
    ACTIVE = 0
    PASSIVE = 1


class ProxyTLSConnect(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/proxy/object#proxy

    Connections to host.
    """
    NO_ENCRYPTION = 1
    PSK = 2
    CERTIFICATE = 4


class ProxyTLSAccept(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/proxy/object#proxy

    Connections from host.
    Possible bitmap values.
    """
    NO_ENCRYPTION = 1
    PSK = 2
    CERTIFICATE = 4


class ProxyCustomTimeouts(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/proxy/object#proxy

    Whether to override global item timeouts on the proxy level.
    """
    USE_GLOBAL = 0
    OVERRIDE = 1


class ProxyCompatibility(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/proxy/object#proxy
    
    Version of proxy compared to Zabbix server version.
    """
    UNDEFINED = 0
    CURRENT_VERSION = 1
    OUTDATED_VERSION  = 2
    UNSUPPORTED_VERSION  = 3


class ProxyState(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/proxy/object#proxy-interface

    State of the proxy.
    """
    UNKNOWN = 0
    OFFLINE = 1
    ONLINE = 2
