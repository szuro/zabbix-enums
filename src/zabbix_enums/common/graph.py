from zabbix_enums.common import _ZabbixEnum


class GraphFlag(_ZabbixEnum):
    PLAIN = 0
    DISCOVERED = 4


class GraphShow3d(_ZabbixEnum):
    NO = 0
    YES = 1


class GraphShowLegend(_ZabbixEnum):
    NO = 0
    YES = 1


class GraphShowWorkPeriod(_ZabbixEnum):
    NO = 0
    YES = 1


class GraphShowTriggers(_ZabbixEnum):
    NO = 0
    YES = 1


class GraphType(_ZabbixEnum):
    NORMAL = 0
    STACKED = 1
    PIE = 2
    EXPLODED = 3


class GraphYmaxType(_ZabbixEnum):
    CALCULATED = 0
    FIXED = 1
    ITEMS = 2


class GraphYminType(_ZabbixEnum):
    CALCULATED = 0
    FIXED = 1
    ITEMS = 2
