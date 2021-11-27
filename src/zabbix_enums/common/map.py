from enum import IntEnum
from . import _NoYes


MapExpandMacro = _NoYes
MapExpandProblem = _NoYes
MapGridAlignEnable = _NoYes
MapGridShow = _NoYes
MapHighlightEnable = _NoYes
MapMarkElements = _NoYes


class MapLabelType(IntEnum):
    LABEL = 0
    IP_ADDRESS = 1
    ELEMENT_NAME = 2
    STATUS = 3
    NOTHING = 4


class MapLabelTypeHost(IntEnum):
    LABEL = 0
    IP_ADDRESS = 1
    ELEMENT_NAME = 2
    STATUS = 3
    NOTHING = 4
    CUSTOM = 5


class MapLabelTypeHostGroup(IntEnum):
    LABEL = 0
    ELEMENT_NAME = 2
    STATUS = 3
    NOTHING = 4
    CUSTOM = 5


class MapLabelTypeImage(IntEnum):
    LABEL = 0
    ELEMENT_NAME = 2
    NOTHING = 4
    CUSTOM = 5


class MapLabelTypeMap(IntEnum):
    LABEL = 0
    ELEMENT_NAME = 2
    STATUS = 3
    NOTHING = 4
    CUSTOM = 5


class MapLabelTypeTrigger(IntEnum):
    LABEL = 0
    ELEMENT_NAME = 2
    STATUS = 3
    NOTHING = 4
    CUSTOM = 5
