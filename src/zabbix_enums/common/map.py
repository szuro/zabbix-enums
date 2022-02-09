from enum import IntEnum


class MapExpandMacro(IntEnum):
    NO = 0
    YES = 1


class MapExpandProblem(IntEnum):
    NO = 0
    YES = 1


class MapGridAlignEnable(IntEnum):
    NO = 0
    YES = 1


class MapGridShow(IntEnum):
    NO = 0
    YES = 1


class MapHighlightEnable(IntEnum):
    NO = 0
    YES = 1


class MapMarkElements(IntEnum):
    NO = 0
    YES = 1


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
