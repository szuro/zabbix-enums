from enum import Enum, IntEnum
from ._common import NoYes, Permission


DashboardPrivate = NoYes
DashboardUserGroupPermission = Permission
DashboardUserPermission = Permission
DashboardWidgetHeaderHidden = NoYes


class DashboardWidgetField(IntEnum):
    INTEGER = 0
    STRING = 1
    HOST_GROUP = 2
    HOST = 3
    ITEM = 4
    GRAPH = 6
    MAP = 8
