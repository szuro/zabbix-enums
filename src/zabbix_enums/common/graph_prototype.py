from zabbix_enums.common import _ZabbixEnum
from .graph import *


GraphPrototypeShow3d = GraphShow3d
GraphPrototypeShowLegend = GraphShowLegend
GraphPrototypeShowWorkPeriod = GraphShowWorkPeriod
GraphPrototypeShowTriggers = GraphShowTriggers
GraphPrototypeType = GraphType
GraphPrototypeYmaxType = GraphYmaxType
GraphPrototypeYminType = GraphYminType


class GrapPrototypeDiscover(_ZabbixEnum):
    DISCOVER = 0
    DONT_DISCOVER = 1
