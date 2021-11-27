from enum import Enum
from zabbix_enums.common import _NoYes


DashboardStartSlideshow = _NoYes


class DashboardWidgetType(str, Enum):
    ACTION_LOG = "actionlog"
    CLOCK = "clock"
    DATA_OVERVIEW = "dataover"
    DISCOVERY_STATUS = "discovery"
    FAVORITE_GRAPHS = "favgraphs"
    FAVORITE_MAPS = "favmaps"
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
