from zabbix_enums.common import _ZabbixEnum


class MacroType(_ZabbixEnum):
    TEXT = 0
    SECRET = 1
    VAULT = 2
