from zabbix_enums.common import _ZabbixEnum


class PreprocessingErrorHandler(_ZabbixEnum):
    ERROR_MESSAGE = 0
    DISCARD_VALUE = 1
    CUSTOM_VALUE = 2
    CUSTOM_ERROR_MESSAGE = 3
