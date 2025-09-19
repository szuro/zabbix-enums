"""https://www.zabbix.com/documentation/7.4/en/manual/api/reference/event/object"""
from zabbix_enums import _ZabbixEnum


class EventSource(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/event/object#event

    Type of the event.
    """
    TRIGGER = 0
    DISCOVERY = 1
    AUTOREGISTRATION = 2
    INTERNAL = 3
    SERVICE = 4


class EventObjectTrigger(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/event/object#event

    Type of object that is related to the event.
    Possible values for trigger events.
    """
    TRIGGER = 0


class EventObjectDiscovery(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/event/object#event

    Type of object that is related to the event.
    Possible values for discovery events.
    """
    HOST = 1
    SERVICE = 2


class EventObjectAutoregistration(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/event/object#event

    Type of object that is related to the event.
    Possible values for autoregistration events.
    """
    HOST = 3


class EventObjectInternal(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/event/object#event

    Possible values for internal events.
    """
    TRIGGER = 0
    ITEM = 4
    LLD = 5


class EventObjectInternal(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/event/object#event

    Possible values for service events.
    """
    SERVICE = 6


class EventValueTrigger(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/event/object#event

    State of the related object.
    Possible values for trigger events.
    """
    OK = 0
    PROBLEM = 1


class EventValueService(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/event/object#event

    State of the related object.
    Possible values for service events.
    """
    OK = 0
    PROBLEM = 1


class EventValueDiscovery(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/event/object#event

    State of the related object.
    Possible values for discovery events.
    """
    UP = 0
    DOWN = 1
    DISCOVERED = 2
    LOST = 3


class EventValueInternal(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/event/object#event

    State of the related object.
    Possible values for internal events.
    """
    NORMAL = 0
    UNKNOWN = 1
    NOT_SUPPORTED = 1


class EventSeverity(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/event/object#event

    Event current severity.
    """
    NOT_CLASSIFIED = 0
    INFORMATION = 1
    WARNING = 2
    AVERAGE = 3
    HIGH = 4
    DISASTER = 5


class EventSuppressed(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/event/object#event

    Whether the event is suppressed.
    """
    NO = 0
    YES = 1
