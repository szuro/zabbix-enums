"""https://www.zabbix.com/documentation/5.2/en/manual/api/reference/screen/object"""
from zabbix_enums import _ZabbixEnum


class ScreenPrivate(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/screen/object#screen

    Type of screen sharing.
    """
    NO = 0
    YES = 1
    PRIVATE = 0
    PUBLIC = 1


class ScreenUserPermission(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/screen/object#screen-user

    Type of permission level.
    """
    READ_ONLY = 2
    READ_WRITE = 3


class ScreenUserGroupPermission(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/screen/object#screen-user-group

    Type of permission level.
    """
    READ_ONLY = 2
    READ_WRITE = 3
