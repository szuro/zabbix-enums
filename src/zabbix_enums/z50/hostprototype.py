"""https://www.zabbix.com/documentation/5.0/en/manual/api/reference/hostprototype/object"""
from zabbix_enums import _ZabbixEnum


class HostPrototypeStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/hostprototype/object#host-prototype

    Status of the host prototype.
    """
    MONITORED = 0
    UNMONITORED = 1


class HostPrototypeInventoryMode(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/hostprototype/object#host-prototype

    Host inventory population mode.
    """
    DISABLED = -1
    MANUAL = 0
    AUTOMATIC = 1


class HostPrototypeDiscover(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/hostprototype/object#host-prototype

    Host prototype discovery status.
    """
    DISCOVER = 0
    DONT_DISCOVER = 1
