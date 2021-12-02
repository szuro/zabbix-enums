from zabbix_enums.common import _ZabbixEnum


class ScriptType(_ZabbixEnum):
    SCRIPT = 0
    IPMI = 1
    SSH = 2
    TELNET = 3
    WEBHOOK = 5


class ScriptScope(_ZabbixEnum):
    ACTION = 1
    MANUAL_HOST = 2
    MANUAL_EVENT = 4
