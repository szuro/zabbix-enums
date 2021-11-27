from enum import Enum, IntEnum
from . import _NoYes, _Permission


DashboardPrivate = _NoYes
DashboardUserGroupPermission = _Permission
DashboardUserPermission = _Permission
DashboardWidgetHeaderHidden = _NoYes


class DashboardWidgetField(IntEnum):
    INTEGER = 0
    STRING = 1
    HOST_GROUP = 2
    HOST = 3
    ITEM = 4
    GRAPH = 6
    MAP = 8
