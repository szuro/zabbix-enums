from zabbix_enums.common import _ZabbixEnum


class HostInterfaceMain(_ZabbixEnum):
    NO = 0
    YES = 1


class HostIntrefaceUseIP(_ZabbixEnum):
    NO = 0
    YES = 1


class HostInterfaceType(_ZabbixEnum):
    AGENT = 1
    SNMP = 2
    IPMI = 3
    JMX = 4
