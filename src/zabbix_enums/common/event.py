from zabbix_enums.common import _ZabbixEnum


class EventSeverity(_ZabbixEnum):
    NOT_CLASSIFIED = 0
    INFORMATION = 1
    WARNING = 2
    AVERAGE = 3
    HIGH = 4
    DISASTER = 5


class EventSuppressed(_ZabbixEnum):
    NO = 0
    YES = 1


class EventObjectTrigger(_ZabbixEnum):
    TRIGGER = 0


class EventObjectInternal(_ZabbixEnum):
    TRIGGER = 0
    ITEM = 4
    LLD = 5


class EventSource(_ZabbixEnum):
    TRIGGER = 0
    DISCOVERY = 1
    AUTOREGISTRATION = 2
    INTERNAL = 3


class EventObjectDiscovery(_ZabbixEnum):
    HOST = 1
    SERVICE = 2


class EventObjectAutoregistration(_ZabbixEnum):
    HOST = 3
