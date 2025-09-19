"""https://www.zabbix.com/documentation/7.4/en/manual/api/reference/templatedashboard/object"""
from enum import Enum
from zabbix_enums import _ZabbixEnum


class TemplateDashboardAutoStart(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/templatedashboard/object#template-dashboard

    Auto start slideshow.
    """
    NO = 0
    YES = 1


TemplateDashboardStartSlideshow = TemplateDashboardAutoStart


class TemplateDashboardWidgetType(str, Enum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/templatedashboard/object#template-dashboard-widget

    Type of the dashboard widget.
    """
    ACTION_LOG = "actionlog"
    CLOCK = "clock"
    DISCOVERY_STATUS = "discovery"
    FAVORITE_GRAPHS = "favgraphs"
    FAVORITE_MAPS = "favmaps"
    GAUGE = "gauge"
    GRAPH_CLASSIC = "graph"
    GRAPH_PROTOTYPE = "graphprototype"
    HONEYCOMB = "honeycomb"
    HOST_AVAILABILITY = "hostavail"
    HOST_CARD = "hostcard"
    HOST_NAVIGATOR = "hostnavigator"
    ITEM_CARD = "itemcard"
    ITEM_NAVIGATOR = "itemnavigator"
    ITEM = "item"
    MAP = "map"
    MAP_NAVIGATION_TREE = "navtree"
    PIECHART = "piechart"
    PLAIN_TEXT = "plaintext"
    PROBLEM_HOSTS = "problemhosts"
    PROBLEMS = "problems"
    PROBLEMS_BY_SEVERITY = "problemsbysv"
    SLA_REPORT = "slareport"
    GRAPH = "svggraph"
    SYSTEM_INFORMATION = "systeminfo"
    TOP_HOSTS = "tophosts"
    TOP_ITEMS = "topitems"
    TOP_TRIGGERS = "toptriggers"
    TRIGGER_OVERVIEW = "trigover"
    URL = "url"
    WEB_MONITORING = "web"


class DashboardWidgetViewMode(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/templatedashboard/object#template-dashboard-widget

    The widget view mode.
    """
    DEFAULT = 0
    HIDDEN_HEADER = 1


class DashboardWidgetFieldType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/templatedashboard/object#template-dashboard-widget-field

    Type of the widget field.
    """
    INTEGER = 0
    STRING = 1
    ITEM = 4
    ITEM_PROTOTYPE = 5
    GRAPH = 6
    GRAPH_PROTOTYPE = 7
    MAP = 8
    SERVICE = 9
    SLA = 10
    USER = 11
    ACTION = 12
    MEDIA_TYPE = 13
