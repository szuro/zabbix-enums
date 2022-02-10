from zabbix_enums.common import _ZabbixEnum


class MapExpandMacro(_ZabbixEnum):
    NO = 0
    YES = 1


class MapExpandProblem(_ZabbixEnum):
    NO = 0
    YES = 1


class MapGridAlignEnable(_ZabbixEnum):
    NO = 0
    YES = 1


class MapGridShow(_ZabbixEnum):
    NO = 0
    YES = 1


class MapHighlightEnable(_ZabbixEnum):
    NO = 0
    YES = 1


class MapMarkElements(_ZabbixEnum):
    NO = 0
    YES = 1


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
