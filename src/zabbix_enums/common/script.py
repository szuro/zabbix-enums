from zabbix_enums.common import _ZabbixEnum


class ScriptExecuteOn(_ZabbixEnum):
    AGENT = 0
    SERVER = 1
    SERVER_PROXY = 2


class ScriptHostAccess(_ZabbixEnum):
    READ = 2
    WRITE = 3
