from . import _ZabbixEnum


class DebugMode(_ZabbixEnum):
    DISABLED = 0
    ENABLED = 1


class GuiAccess(_ZabbixEnum):
    SYSTEM = 0
    INTERNAL = 1
    LDAP = 2
    DISABLED = 3


class UserStatus(_ZabbixEnum):
    ENABLED = 0
    DISABLED = 1



class UserGroupPermission(_ZabbixEnum):
    ACCESS_DENIED = 0
    READ_ONLY = 1
    READ_WRITE = 2

