from zabbix_enums.common import _ZabbixEnum


class ItemFlag(_ZabbixEnum):
    PLAIN = 0
    DISCOVERED = 4


class ItemStatus(_ZabbixEnum):
    ENABLED = 0
    DISABLED = 1


class ItemValueType(_ZabbixEnum):
    NUMERIC_FLOAT = 0
    CHARACTER = 1
    LOG = 2
    NUMERIC_UNSIGNED = 3
    TEXT = 4


class ItemState(_ZabbixEnum):
    NORMAL = 0
    NOT_SUPPORTED = 1


class ItemAuthTypeSSH(_ZabbixEnum):
    PASSWORD = 0
    PUBLIC_KEY = 1
