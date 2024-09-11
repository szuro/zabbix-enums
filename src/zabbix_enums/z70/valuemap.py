"""https://www.zabbix.com/documentation/7.0/en/manual/api/reference/valuemap/object"""
from zabbix_enums import _ZabbixEnum


class ValueMappingsType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/valuemap/object#value-mappings

    Mapping match type.
    """
    EXACT_MATCH = 0
    GREATER_OR_EQUAL = 1
    LESS_OR_EQUAL = 2
    IN_RANGE = 3
    REGEX = 4
    DEFAULT = 5
