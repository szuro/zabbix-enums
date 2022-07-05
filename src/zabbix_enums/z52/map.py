"""https://www.zabbix.com/documentation/5.2/en/manual/api/reference/map/object"""
from zabbix_enums import _ZabbixEnum


class MapExpandMacro(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/map/object#map

    Whether to expand macros in labels when configuring the map.
    """
    NO = 0
    YES = 1


class MapExpandProblem(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/map/object#map

    Whether the problem trigger will be displayed for elements with a single problem.
    """
    NO = 0
    YES = 1


class MapGridAlign(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/map/object#map

    Whether to enable grid aligning.
    """
    NO = 0
    YES = 1


class MapGridShow(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/map/object#map

    Whether to show the grid on the map.
    """
    NO = 0
    YES = 1


class MapHighlight(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/map/object#map

    Whether icon highlighting is enabled.
    """
    NO = 0
    YES = 1


class MapLabelFormat(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/map/object#map

    Whether to enable advanced labels.
    """
    DISABLE_ADVANCED_LABELS = 0
    ENABLE_ADVANCED_LABELS = 1


class MapLabelLocation(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/map/object#map

    Location of the map element label.
    """
    BOTTOM = 0
    LEFT = 1
    RIGHT = 2
    TOP = 3


class MapLabelType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/map/object#map

    Map element label type.
    """
    LABEL = 0
    IP_ADDRESS = 1
    ELEMENT_NAME = 2
    STATUS = 3
    NOTHING = 4


class MapLabelTypeHost(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/map/object#map

    Label type for host elements.
    """
    LABEL = 0
    IP_ADDRESS = 1
    ELEMENT_NAME = 2
    STATUS = 3
    NOTHING = 4
    CUSTOM = 5


class MapLabelTypeHostGroup(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/map/object#map

    Label type for host group elements.
    """
    LABEL = 0
    ELEMENT_NAME = 2
    STATUS = 3
    NOTHING = 4
    CUSTOM = 5


class MapLabelTypeImage(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/map/object#map

    Label type for host group elements.
    """
    LABEL = 0
    ELEMENT_NAME = 2
    NOTHING = 4
    CUSTOM = 5


class MapLabelTypeMap(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/map/object#map

    Label type for map elements.
    """
    LABEL = 0
    ELEMENT_NAME = 2
    STATUS = 3
    NOTHING = 4
    CUSTOM = 5


class MapLabelTypeTrigger(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/map/object#map

    Label type for trigger elements.
    """
    LABEL = 0
    ELEMENT_NAME = 2
    STATUS = 3
    NOTHING = 4
    CUSTOM = 5


class MapMarkElements(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/map/object#map

    Whether to highlight map elements that have recently changed their status.
    """
    NO = 0
    YES = 1


class MapShowUnack(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/map/object#map

    How problems should be displayed.
    """
    COUNT_ALL_PROBLEMS = 0
    COUNT_UNACK_PROBLEMS = 1
    COUNT_ALL_PROBLEMS_SEPARATELY = 2


class MapPrivate(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/map/object#map

    Type of map sharing.
    """
    NO = 0
    YES = 1


class MapShowSuppressed(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/map/object#map

    Whether suppressed problems are shown.
    """
    NO = 0
    YES = 1
