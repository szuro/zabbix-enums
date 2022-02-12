from zabbix_enums.common import _ZabbixEnum


class GraphItemCalcFnc(_ZabbixEnum):
    MINIMUM_VALUE = 1
    AVERAGE_VALUE = 2
    MAXIMUM_VALUE = 4
    ALL_VALUES = 7
    LAST_VALUE = 9


class GraphItemDrawType(_ZabbixEnum):
    LINE = 0
    FILLED_REGION = 1
    BOLD_LINE = 2
    DOT = 3
    DASHED_LINE = 4
    GRADIENT_LINE = 5


class GraphItemType(_ZabbixEnum):
    SIMPLE = 0
    GRAPH_SUM = 2


class GraphItemYaxisSide(_ZabbixEnum):
    LEFT = 0
    RIGHT = 1
