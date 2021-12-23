from enum import IntEnum


class DashboardPrivate(IntEnum):
    NO = 0
    YES = 1


class DashboardUserGroupPermission(IntEnum):
    READ_ONLY = 2
    READ_WRITE = 3


class DashboardUserPermission(IntEnum):
    READ_ONLY = 2
    READ_WRITE = 3


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
