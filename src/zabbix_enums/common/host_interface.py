from . import _NoYes, _ZabbixEnum


HostInterfaceMain = _NoYes
HostIntrefaceUseIP = _NoYes


class HostInterfaceType(_ZabbixEnum):
    AGENT = 1
    SNMP = 2
    IPMI = 3
    JMX = 4
