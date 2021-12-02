from . import _NoYes,_ZabbixEnum


class ProxyStatus(_ZabbixEnum):
    ACTIVE = 5
    PASSIVE = 6

ProxyType = ProxyStatus
ProxyUseIp = _NoYes
