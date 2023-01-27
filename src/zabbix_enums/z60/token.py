"""https://www.zabbix.com/documentation/6.0/en/manual/api/reference/token/object"""
from zabbix_enums import _ZabbixEnum


class TokenStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.0/en/manual/api/reference/token/object#token

    Token status.
    """
    ENABLED = 0
    DISABLED = 1
