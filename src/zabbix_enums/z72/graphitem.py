"""https://www.zabbix.com/documentation/7.2/en/manual/api/reference/graphitem/object"""
from zabbix_enums import _ZabbixEnum


class GraphItemCalcFnc(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.2/en/manual/api/reference/graphitem/object#graph-item
    
    Value of the item that will be displayed.
    """
    MINIMUM_VALUE = 1
    AVERAGE_VALUE = 2
    MAXIMUM_VALUE = 4
    ALL_VALUES = 7
    LAST_VALUE = 9


class GraphItemDrawType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.2/en/manual/api/reference/graphitem/object#graph-item
    
    Draw style of the graph item.
    """
    LINE = 0
    FILLED_REGION = 1
    BOLD_LINE = 2
    DOT = 3
    DASHED_LINE = 4
    GRADIENT_LINE = 5


class GraphItemType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.2/en/manual/api/reference/graphitem/object#graph-item
    
    Type of graph item.
    """
    SIMPLE = 0
    GRAPH_SUM = 2


class GraphItemYaxisSide(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.2/en/manual/api/reference/graphitem/object#graph-item
    
    Side of the graph where the graph item's Y scale will be drawn.
    """
    LEFT = 0
    RIGHT = 1
