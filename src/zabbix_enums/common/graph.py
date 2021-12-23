from enum import IntEnum
from . import _DiscoveryFlag


GraphFlag = _DiscoveryFlag


class GraphShow3d(IntEnum):
    NO = 0
    YES = 1


class GraphShowLegend(IntEnum):
    NO = 0
    YES = 1


class GraphShowWorkPeriod(IntEnum):
    NO = 0
    YES = 1


class GraphShowTriggers(IntEnum):
    NO = 0
    YES = 1


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
