"""https://www.zabbix.com/documentation/7.0/en/manual/api/reference/graph/object"""
from zabbix_enums import _ZabbixEnum


class GraphFlag(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/graph/object#graph

    [Readonly]
    Origin of the graph.
    """
    PLAIN = 0
    DISCOVERED = 4


class GraphType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/graph/object#graph

    Graph's layout type.
    """
    NORMAL = 0
    STACKED = 1
    PIE = 2
    EXPLODED = 3


class GraphShow3d(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/graph/object#graph

    Whether to show pie and exploded graphs in 3D.
    """
    NO = 0
    YES = 1
    SHOW_IN_2D = 0
    SHOW_IN_3D = 1


class GraphShowLegend(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/graph/object#graph

    Whether to show the legend on the graph.
    """
    NO = 0
    YES = 1
    HIDE = 0
    SHOW = 1


class GraphShowWorkPeriod(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/graph/object#graph

    Whether to show the working time on the graph.
    """
    NO = 0
    YES = 1
    HIDE = 0
    SHOW = 1


class GraphShowTriggers(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/graph/object#graph

    Whether to show the trigger line on the graph.
    """
    NO = 0
    YES = 1
    HIDE = 0
    SHOW = 1


class GraphYmaxType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/graph/object#graph

    Maximum value calculation method for the Y axis.
    """
    CALCULATED = 0
    FIXED = 1
    ITEM = 2


class GraphYminType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/graph/object#graph

    Minimum value calculation method for the Y axis.
    """
    CALCULATED = 0
    FIXED = 1
    ITEM = 2
