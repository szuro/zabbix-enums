"""https://www.zabbix.com/documentation/5.0/en/manual/api/reference/dashboard/object"""
from enum import Enum
from unittest.mock import DEFAULT
from zabbix_enums import _ZabbixEnum


class DashboardPrivate(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/dashboard/object#dashboard

    Type of dashboard sharing.
    """
    NO = 0
    YES = 1
    PUBLIC = 0
    PRIVATE = 1


class DashboardWidgetType(str, Enum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/dashboard/object#dashboard-widget

    Type of the dashboard widget.
    """
    ACTION_LOG = "actionlog"
    CLOCK = "clock"
    DATA_OVERVIEW = "dataover"
    DISCOVERY_STATUS = "discovery"
    FAVORITE_GRAPHS = "favgraphs"
    FAVORITE_MAPS = "favmaps"
    FAVORITE_SCREENS = "favscreens"
    GRAPH_CLASSIC = "graph"
    GRAPH_PROTOTYPE = "graphprototype"
    HOST_AVAILABILITY = "hostavail"
    MAP = "map"
    MAP_NAVIGATION_TREE = "navtree"
    PLAIN_TEXT = "plaintext"
    PROBLEM_HOSTS = "problemhosts"
    PROBLEMS = "problems"
    PROBLEMS_BY_SEVERITY = "problemsbysv"
    GRAPH = "svggraph"
    SYSTEM_INFORMATION = "systeminfo"
    TRIGGER_OVERVIEW = "trigover"
    URL = "url"
    WEB_MONITORING = "web"


class DashboardWidgetViewMode(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/dashboard/object#dashboard-widget

    The widget view mode.
    """
    DEFAULT = 0
    HIDDEN_HEADER = 1


class DashboardWidgetFieldType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/dashboard/object#dashboard-widget-field

    Type of the widget field.
    """
    INTEGER = 0
    STRING = 1
    HOST_GROUP = 2
    HOST = 3
    ITEM = 4
    GRAPH = 6
    MAP = 8


class DashboardUserGroupPermission(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/dashboard/object#dashboard-user-group

    Type of permission level.
    """
    READ_ONLY = 2
    READ_WRITE = 3


class DashboardUserPermission(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/dashboard/object#dashboard-user

    Type of permission level.
    """
    READ_ONLY = 2
    READ_WRITE = 3
