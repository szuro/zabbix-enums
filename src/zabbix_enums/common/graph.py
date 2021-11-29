from enum import IntEnum
from . import _DiscoveryFlag, _NoYes


GraphFlag = _DiscoveryFlag
GraphShow3d = _NoYes
GraphShowLegend = _NoYes
GraphShowWorkPeriod = _NoYes
GraphShowTriggers = _NoYes


class GraphType(IntEnum):
    NORMAL = 0
    STACKED = 1
    PIE = 2
    EXPLODED = 3


class GraphYmaxType(IntEnum):
    CALCULATED = 0
    FIXED = 1
    ITEMS = 2

GraphYminType = GraphYmaxType
