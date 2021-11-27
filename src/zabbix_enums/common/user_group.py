from enum import IntEnum


class DebugMode(IntEnum):
    DISABLED = 0
    ENABLED = 1


class GuiAccess(IntEnum):
    SYSTEM = 0
    INTERNAL = 1
    LDAP = 2
    DISABLED = 3


class UserStatus(IntEnum):
    ENABLED = 0
    DISABLED = 1



class UserGroupPermission(IntEnum):
    ACCESS_DENIED = 0
    READ_ONLY = 1
    READ_WRITE = 2

