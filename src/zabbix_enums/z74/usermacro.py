"""https://www.zabbix.com/documentation/7.4/en/manual/api/reference/usermacro/object"""
from zabbix_enums import _ZabbixEnum


class GlobalMacroType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/usermacro/object#global-macro

    Type of macro.
    """
    TEXT = 0
    SECRET = 1
    VAULT = 2


class HostMacroType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/usermacro/object#host-macro

    Type of macro.
    """
    TEXT = 0
    SECRET = 1
    VAULT = 2


class HostMacroAutomatic(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/usermacro/object#host-macro
    
    Defines whether the macro is controlled by discovery rule.
    User is not allowed to create automatic macro.
    To update automatic macro, it must be converted to manual.
    """
    NO = 0
    YES = 1


class MacroConfigurationType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/usermacro/object#macro-configuration

    Type of macro input field.
    """
    UNUSED = 0
    TEXTBOX = 1
    LIST = 2
    CHECKBOX = 3

class MacroConfigurationRequired(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/usermacro/object#macro-configuration

    Type of macro input field.
    """
    NO = 0
    YES = 1
