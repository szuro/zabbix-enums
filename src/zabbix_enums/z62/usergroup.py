"""https://www.zabbix.com/documentation/6.2/en/manual/api/reference/usergroup/object"""
from zabbix_enums import _ZabbixEnum


class UserGroupDebugMode(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/usergroup/object#user-group
    
    Whether debug mode is enabled or disabled.
    """
    DISABLED = 0
    ENABLED = 1


class UserGroupGuiAccess(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/usergroup/object#user-group
    
    Frontend authentication method of the users in the group.
    """
    SYSTEM = 0
    INTERNAL = 1
    LDAP = 2
    DISABLED = 3


class UserGroupUsersStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/usergroup/object#user-group
    
    Whether the user group is enabled or disabled.
    """
    ENABLED = 0
    DISABLED = 1



class Permission(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/usergroup/object#permission
    
    
    Access level to the host group.
    """
    ACCESS_DENIED = 0
    READ_ONLY = 1
    READ_WRITE = 2

