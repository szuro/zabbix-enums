from . import _NoYes, _ZabbixEnum


MapExpandMacro = _NoYes
MapExpandProblem = _NoYes
MapGridAlignEnable = _NoYes
MapGridShow = _NoYes
MapHighlightEnable = _NoYes
MapMarkElements = _NoYes


class MapLabelType(_ZabbixEnum):
    LABEL = 0
    IP_ADDRESS = 1
    ELEMENT_NAME = 2
    STATUS = 3
    NOTHING = 4


class MapLabelTypeHost(_ZabbixEnum):
    LABEL = 0
    IP_ADDRESS = 1
    ELEMENT_NAME = 2
    STATUS = 3
    NOTHING = 4
    CUSTOM = 5


class MapLabelTypeHostGroup(_ZabbixEnum):
    LABEL = 0
    ELEMENT_NAME = 2
    STATUS = 3
    NOTHING = 4
    CUSTOM = 5


class MapLabelTypeImage(_ZabbixEnum):
    LABEL = 0
    ELEMENT_NAME = 2
    NOTHING = 4
    CUSTOM = 5


class MapLabelTypeMap(_ZabbixEnum):
    LABEL = 0
    ELEMENT_NAME = 2
    STATUS = 3
    NOTHING = 4
    CUSTOM = 5


class MapLabelTypeTrigger(_ZabbixEnum):
    LABEL = 0
    ELEMENT_NAME = 2
    STATUS = 3
    NOTHING = 4
    CUSTOM = 5
