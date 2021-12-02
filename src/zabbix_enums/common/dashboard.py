from . import _NoYes, _Permission, _ZabbixEnum


DashboardPrivate = _NoYes
DashboardUserGroupPermission = _Permission
DashboardUserPermission = _Permission
DashboardWidgetHeaderHidden = _NoYes


class DashboardWidgetField(_ZabbixEnum):
    INTEGER = 0
    STRING = 1
    HOST_GROUP = 2
    HOST = 3
    ITEM = 4
    GRAPH = 6
    MAP = 8
