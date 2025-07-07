"""https://www.zabbix.com/documentation/7.4/en/manual/api/reference/map/object"""
from zabbix_enums import _ZabbixEnum


class MapBackgroundScale(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/map/object#map

    Whether to enable background image proportional scaling.
    """
    NO = 0
    YES = 1


class MapExpandMacro(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/map/object#map

    Whether to expand macros in labels when configuring the map.
    """
    NO = 0
    YES = 1


class MapExpandProblem(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/map/object#map

    Whether the problem trigger will be displayed for elements with a single problem.
    """
    NO = 0
    YES = 1


class MapGridAlign(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/map/object#map

    Whether to enable grid aligning.
    """
    NO = 0
    YES = 1


class MapGridShow(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/map/object#map

    Whether to show the grid on the map.
    """
    NO = 0
    YES = 1


class MapHighlight(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/map/object#map

    Whether icon highlighting is enabled.
    """
    NO = 0
    YES = 1


class MapLabelFormat(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/map/object#map

    Whether to enable advanced labels.
    """
    DISABLE_ADVANCED_LABELS = 0
    ENABLE_ADVANCED_LABELS = 1


class MapLabelLocation(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/map/object#map

    Location of the map element label.
    """
    BOTTOM = 0
    LEFT = 1
    RIGHT = 2
    TOP = 3


class MapLabelType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/map/object#map

    Map element label type.
    """
    LABEL = 0
    IP_ADDRESS = 1
    ELEMENT_NAME = 2
    STATUS = 3
    NOTHING = 4


class MapLabelTypeHost(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/map/object#map

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
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/map/object#map

    Label type for host group elements.
    """
    LABEL = 0
    ELEMENT_NAME = 2
    STATUS = 3
    NOTHING = 4
    CUSTOM = 5


class MapLabelTypeImage(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/map/object#map

    Label type for host group elements.
    """
    LABEL = 0
    ELEMENT_NAME = 2
    NOTHING = 4
    CUSTOM = 5


class MapLabelTypeMap(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/map/object#map

    Label type for map elements.
    """
    LABEL = 0
    ELEMENT_NAME = 2
    STATUS = 3
    NOTHING = 4
    CUSTOM = 5


class MapLabelTypeTrigger(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/map/object#map

    Label type for trigger elements.
    """
    LABEL = 0
    ELEMENT_NAME = 2
    STATUS = 3
    NOTHING = 4
    CUSTOM = 5


class MapMarkElements(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/map/object#map

    Whether to highlight map elements that have recently changed their status.
    """
    NO = 0
    YES = 1

class MapShowElementLabel(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/map/object#map

    How to display element labels by default.
    """
    ALWAYS = 0
    AUTO_HIDE = 1


class MapShowLinkLabel(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/map/object#map

    How to display link labels by default.
    """
    ALWAYS = 0
    AUTO_HIDE = 1


class MapShowUnack(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/map/object#map

    How problems should be displayed.
    """
    COUNT_ALL_PROBLEMS = 0
    COUNT_UNACK_PROBLEMS = 1
    COUNT_ALL_PROBLEMS_SEPARATELY = 2


class MapPrivate(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/map/object#map

    Type of map sharing.
    """
    NO = 0
    YES = 1


class MapShowSuppressed(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/map/object#map

    Whether suppressed problems are shown.
    """
    NO = 0
    YES = 1


class MapLinkShowLabel(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/map/object#map-link

    How to display the element label.
    """
    DEFAULT = -1
    ALWAYS = 0
    AUTO_HIDE = 1


class MapLinkIndicatorType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/map/object#map-link

    Select the link indicator type.
    """
    STATIC_LINK = 0
    TRIGGER = 1
    ITEM_VALUE = 2



class MapLinkTriggerDrawtype(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/map/object#map-link-trigger

    Indicator draw style.
    """
    LINE = 0
    BOLD_LINE = 2
    DOTTED_LINE = 3
    DASHED_LINE = 4


class MapLinkIndicatorDrawtype(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/map/object#map-link-indicators

    Indicator draw style.
    """
    LINE = 0
    BOLD_LINE = 2
    DOTTED_LINE = 3
    DASHED_LINE = 4