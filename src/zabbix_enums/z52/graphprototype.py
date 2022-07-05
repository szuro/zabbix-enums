"""https://www.zabbix.com/documentation/5.2/en/manual/api/reference/graphprototype/object"""
from zabbix_enums import _ZabbixEnum


class GraphPrototypeType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/graphprototype/object#graph-prototype

    Graph prototypes's layout type.
    """
    NORMAL = 0
    STACKED = 1
    PIE = 2
    EXPLODED = 3


class GraphPrototypeShow3d(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/graphprototype/object#graph-prototype

    Whether to show discovered pie and exploded graphs in 3D.
    """
    NO = 0
    YES = 1
    SHOW_IN_2D = 0
    SHOW_IN_3D = 1


class GraphPrototypeShowLegend(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/graphprototype/object#graph-prototype

    Whether to show the legend on the discovered graph.
    """
    NO = 0
    YES = 1
    HIDE = 0
    SHOW = 1


class GraphPrototypeShowWorkPeriod(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/graphprototype/object#graph-prototype

    Whether to show the working time on the discovered graph.
    """
    NO = 0
    YES = 1
    HIDE = 0
    SHOW = 1


class GraphPrototypeYmaxType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/graphprototype/object#graph-prototype

    Maximum value calculation method for the Y axis.
    """
    CALCULATED = 0
    FIXED = 1
    ITEM = 2


class GraphPrototypeYminType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/graphprototype/object#graph-prototype

    Minimum value calculation method for the Y axis.
    """
    CALCULATED = 0
    FIXED = 1
    ITEM = 2


class GrapPrototypeDiscover(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/graphprototype/object#graph-prototype-prototype

    Graph prototype discovery status.
    """
    DISCOVER = 0
    DONT_DISCOVER = 1
