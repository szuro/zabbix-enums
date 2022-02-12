from zabbix_enums.common import _ZabbixEnum


class DashboardPrivate(_ZabbixEnum):
    NO = 0
    YES = 1


class DashboardUserGroupPermission(_ZabbixEnum):
    READ_ONLY = 2
    READ_WRITE = 3


class DashboardUserPermission(_ZabbixEnum):
    READ_ONLY = 2
    READ_WRITE = 3


class DashboardWidgetHeaderHidden(_ZabbixEnum):
    NO = 0
    YES = 1


class DashboardWidgetField(_ZabbixEnum):
    INTEGER = 0
    STRING = 1
    HOST_GROUP = 2
    HOST = 3
    ITEM = 4
    GRAPH = 6
    MAP = 8
