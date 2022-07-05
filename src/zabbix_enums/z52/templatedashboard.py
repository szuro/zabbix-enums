"""https://www.zabbix.com/documentation/5.2/en/manual/api/reference/templatedashboard/object"""
from enum import Enum
from zabbix_enums import _ZabbixEnum


class TemplateDashboardWidgetType(str, Enum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/templatedashboard/object#template-dashboard-widget

    Type of the dashboard widget.
    """
    CLOCK = "clock"
    GRAPH_CLASSIC = "graph"
    GRAPH_PROTOTYPE = "graphprototype"
    PLAIN_TEXT = "plaintext"
    URL = "url"


class DashboardWidgetViewMode(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/templatedashboard/object#template-dashboard-widget

    The widget view mode.
    """
    DEFAULT = 0
    HIDDEN_HEADER = 1


class DashboardWidgetField(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/templatedashboard/object#template-dashboard-widget

    Type of the widget field.
    """
    INTEGER = 0
    STRING = 1
    ITEM = 4
    ITEM_PROTOTYPE = 5
    GRAPH = 6
    GRAPH_PROTOTYPE = 7
