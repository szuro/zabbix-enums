"""https://www.zabbix.com/documentation/5.2/en/manual/api/reference/screenitem/object"""
from zabbix_enums import _ZabbixEnum


class ScreenItemResourceType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/screenitem/object#screen-item

    Type of screen item.
    """
    GRAPH = 0
    SIMPLE_GRAPH = 1
    MAP = 2
    PLAIN_TEXT = 3
    HOSTS_INFO = 4
    TRIGGERS_INFO = 5
    SYSTEM_INFORMATION = 6
    CLOCK = 7
    TRIGGERS_OVERVIEW = 9
    DATA_OVERVIEW = 10
    URL = 11
    HISTORY_OF_ACTIONS = 12
    HISTORY_OF_EVENTS = 13
    LATEST_HOST_GROUP_ISSUES = 14
    PROBLEMS_BY_SEVERITY = 15
    LATEST_HOST_ISSUES = 16
    SIMPLE_GRAPH_PROTOTYPE = 19
    GRAPH_PROTOTYPE = 20


class ScreenItemDynamic(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/screenitem/object#screen-item

    Whether the screen item is dynamic.
    """
    NO = 0
    YES = 1


class ScreenItemHalign(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/screenitem/object#screen-item

    Specifies how the screen item must be aligned horizontally in the cell.
    """
    CENTER = 0
    LEFT = 1
    RIGHT = 2


class ScreenItemSortTriggersActions(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/screenitem/object#screen-item

    Order in which actions or triggers must be sorted.
    Possible values for history of actions screen elements.
    """
    TIME_ASCENDING = 3
    TIME_DESCENDING = 4
    TYPE_ASCENDING = 5
    TYPE_DESCENDING = 6
    STATUS_ASCENDING = 7
    STATUS_DESCENDING = 8
    RETRIES_LEFT_ASCENDING = 9
    RETRIES_LEFT_DESCENDING = 10
    RECIPIENT_ASCENDING = 11
    RECIPIENT_DESCENDING = 12


class ScreenItemSortTriggersIssues(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/screenitem/object#screen-item

    Possible values for latest host group issues and latest host issues screen items:
    """
    LAST_CHANGE_DESCENDING = 0
    SEVERITY_DESCENDING = 1
    HOST_ASCENDING = 2


class ScreenItemStyleOverview(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/screenitem/object#screen-item

    Screen item display option.
    Possible values for data overview and triggers overview screen items:
    """
    HOSTS_ON_LEFT = 0
    HOSTS_ON_TOP = 1


class ScreenItemStyleInfo(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/screenitem/object#screen-item

    Screen item display option.
    Possible values for hosts info and triggers info screen elements.
    """

    HORIZONTAL_LAYOUT = 0
    VERTICAL_LAYOUT = 1


class ScreenItemStyleClock(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/screenitem/object#screen-item

    Screen item display option.
    Possible values for clock screen items.
    """
    LOCAL_TIME = 0
    SERVER_TIME = 1
    HOST_TIME = 2


class ScreenItemStylePlaintext(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/screenitem/object#screen-item

    Screen item display option.
    Possible values for plain text screen items.
    """
    PLAIN = 0
    HTML = 1


class ScreenItemValign(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/screenitem/object#screen-item

    Specifies how the screen item must be aligned vertically in the cell.
    """
    MIDDLE = 0
    TOP = 1
    BOTTOM = 2
