from . import _PrototypeDiscover
from .graph import *


class GraphPrototypeShow3d(IntEnum):
    NO = 0
    YES = 1


class GraphPrototypeShowLegend(IntEnum):
    NO = 0
    YES = 1


class GraphPrototypeShowWorkPeriod(IntEnum):
    NO = 0
    YES = 1


class GraphPrototypeShowTriggers(IntEnum):
    NO = 0
    YES = 1


GraphPrototypeType = GraphType
GraphPrototypeYmaxType = GraphYmaxType
GraphPrototypeYminType = GraphPrototypeYmaxType
GrapPrototypeDiscover = _PrototypeDiscover
