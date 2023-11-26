"""https://www.zabbix.com/documentation/6.2/en/manual/api/reference/usermacro/object"""
from zabbix_enums import _ZabbixEnum


class GlobalMacroType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/usermacro/object#global-macro

    Type of macro.
    """
    TEXT = 0
    SECRET = 1
    VAULT = 2


class HostMacroType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/usermacro/object#host-macro

    Type of macro.
    """
    TEXT = 0
    SECRET = 1
    VAULT = 2


class HostMacroAutomatic(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/usermacro/object#host-macro
    
    Defines whether the macro is controlled by discovery rule.
    User is not allowed to create automatic macro.
    To update automatic macro, it must be converted to manual.
    """
    NO = 0
    YES = 1
