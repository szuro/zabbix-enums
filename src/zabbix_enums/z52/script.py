"""https://www.zabbix.com/documentation/5.2/en/manual/api/reference/script/object"""
from zabbix_enums import _ZabbixEnum


class ScriptExecuteOn(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/script/object#script

    Where to run the script.
    """
    AGENT = 0
    SERVER = 1
    SERVER_PROXY = 2


class ScriptHostAccess(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/script/object#script

    Host permissions needed to run the script.
    """
    READ = 2
    WRITE = 3


class ScriptType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/script/object#script

    Script type.
    """
    SCRIPT = 0
    IPMI = 1
