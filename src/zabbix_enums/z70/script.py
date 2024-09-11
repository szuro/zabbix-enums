"""https://www.zabbix.com/documentation/7.0/en/manual/api/reference/script/object"""
from zabbix_enums import _ZabbixEnum


class ScriptType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/script/object#script

    Script type.
    """
    SCRIPT = 0
    IPMI = 1
    SSH = 2
    TELNET = 3
    WEBHOOK = 5
    URL = 6


class ScriptScope(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/script/object#script

    Script type.
    """
    ACTION_OPERATION = 1
    HOST_ACTION = 2
    MANUAL_HOST_ACTION = 2
    EVENT_ACTION = 4
    MANUAL_EVENT_ACTION = 4


class ScriptExecuteOn(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/script/object#script

    Where to run the script.
    """
    AGENT = 0
    SERVER = 1
    SERVER_PROXY = 2


class ScriptAuthType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/script/object#script

    Authentication method used for SSH script type.
    Used if type is 2 (SSH).
    """
    PASSWORD = 0
    PUBLIC_KEY = 1


class ScriptHostAccess(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/script/object#script

    Host permissions needed to run the script.
    """
    READ = 2
    WRITE = 3

class ScripNewWindow(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/script/object#script

    Open URL in a new window.
    """
    NO = 0
    YES = 1

class ScripManualInput(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/script/object#script

    Indicates whether the script accepts user-provided input.
    """
    DISABLED = 0
    ENABLED = 1


class ScripManualInputValidatorType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/script/object#script

    Determines the type of user input expected.
    """
    STRING = 0
    LIST = 1
