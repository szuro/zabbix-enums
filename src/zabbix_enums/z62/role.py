"""https://www.zabbix.com/documentation/6.2/en/manual/api/reference/role/object"""
from zabbix_enums import _ZabbixEnum


class RoleType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/role/object#role

    User type.
    """
    USER = 1
    ADMIN = 2
    SUPERADMIN = 3


class RoleReadOnly(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/role/object#role

    [Readonly]
    Whether the role is readonly.
    """
    NO = 0
    YES = 1


class RoleRulesUIDefaultAccess(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/role/object#role-rules

    Whether access to new UI elements is enabled.
    """
    DISABLED = 0
    ENABLED = 1


class RoleRulesModulesDefaultAccess(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/role/object#role-rules

    Whether access to new modules is enabled.
    """
    DISABLED = 0
    ENABLED = 1


class RoleRulesAPIAccess(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/role/object#role-rules

    Whether access to API is enabled.
    """
    DISABLED = 0
    ENABLED = 1


class RoleRulesAPIMode(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/role/object#role-rules

    Mode for treating API methods listed in the api property.
    """
    DENY_LIST = 0
    ALLOW_LIST = 1


class RoleRulesActionsDefaultAccess(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/role/object#role-rules

    Whether access to new actions is enabled.
    """
    DISABLED = 0
    ENABLED = 1


class UIElementStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/role/object#ui-element

    Whether access to the UI element is enabled.
    """
    DISABLED = 0
    ENABLED = 1


class ModuleStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/role/object#module

    Whether access to the module is enabled.
    """
    DISABLED = 0
    ENABLED = 1


class ActionStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/role/object#action

    Whether access to perform the action is enabled.
    """
    DISABLED = 0
    ENABLED = 1
