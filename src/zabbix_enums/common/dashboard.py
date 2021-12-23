from enum import IntEnum
from . import _Permission


class DashboardPrivate(IntEnum):
    NO = 0
    YES = 1

DashboardUserGroupPermission = _Permission
DashboardUserPermission = _Permission

class DashboardWidgetHeaderHidden(IntEnum):
    NO = 0
    YES = 1


class DashboardWidgetField(IntEnum):
    INTEGER = 0
    STRING = 1
    HOST_GROUP = 2
    HOST = 3
    ITEM = 4
    GRAPH = 6
    MAP = 8
