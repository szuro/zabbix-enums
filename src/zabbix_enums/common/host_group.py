from zabbix_enums.common import _ZabbixEnum


class HostGroupFlag(_ZabbixEnum):
    PLAIN = 0
    DISCOVERED = 4


class HostGroupInternal(_ZabbixEnum):
    NO = 0
    YES = 1
