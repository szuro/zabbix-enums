"""https://www.zabbix.com/documentation/5.0/en/manual/api/reference/templatescreenitem/object"""
from zabbix_enums import _ZabbixEnum


class TemplateScreenItemReourceType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/templatescreenitem/object#template-screen-item

    Type of template screen item.
    """
    GRAPH = 0
    SIMPLE_GRAPH = 1
    PLAIN_TEXT = 3
    CLOCK = 7
    URL = 11
    SIMPLE_GRAPH_PROTOTYPE = 19
    GRAPH_PROTOTYPE = 20


class TemplateScreenItemHalign(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/templatescreenitem/object#template-screen-item

    Specifies how the template screen item must be aligned horizontally in the cell.
    """
    CENTER = 0
    LEFT = 1
    RIGHT = 2


class TemplateScreenItemStyleClock(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/templatescreenitem/object#template-screen-item

    Template screen item display option.
    Possible values for clock screen items.
    """
    LOCAL_TIME = 0
    SERVER_TIME = 1
    HOST_TIME = 2


class TemplateScreenItemStylePlaintext(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/templatescreenitem/object#template-screen-item

    Template screen item display option.
    Possible values for plain text screen items:
    """
    PLAIN = 0
    HTML = 1


class TemplateScreenItemValign(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/templatescreenitem/object#template-screen-item

    Specifies how the template screen item must be aligned vertically in the cell.
    """
    MIDDLE = 0
    TOP = 1
    BOTTOM = 2
