from zabbix_enums.common import _ZabbixEnum


class ProxyStatus(_ZabbixEnum):
    ACTIVE = 5
    PASSIVE = 6


class ProxyType(_ZabbixEnum):
    ACTIVE = 5
    PASSIVE = 6


class ProxyUseIp(_ZabbixEnum):
    NO = 0
    YES = 1
