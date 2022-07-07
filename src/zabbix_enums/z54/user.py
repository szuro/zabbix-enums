"""https://www.zabbix.com/documentation/5.4/en/manual/api/reference/user/object"""
from zabbix_enums import _ZabbixEnum


class UserAutologin(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.4/en/manual/api/reference/user/object#user

    Whether to enable auto-login.
    """
    NO = 0
    YES = 1


class MediaActive(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.4/en/manual/api/reference/user/object#media

    Whether the media is enabled.
    """
    ENABLED = 0
    DISABLED = 1
