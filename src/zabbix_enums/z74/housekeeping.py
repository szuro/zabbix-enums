"""https://www.zabbix.com/documentation/7.4/en/manual/api/reference/housekeeping/object"""
from zabbix_enums import _ZabbixEnum


class HousekeepingHKEventsMode(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/housekeeping/object#housekeeping

    Enable internal housekeeping for events and alerts.
    """
    DISABLED = 0
    ENABLED = 1


class HousekeepingHKServiceMode(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/housekeeping/object#housekeeping

    Enable internal housekeeping for services.
    """
    DISABLED = 0
    ENABLED = 1


class HousekeepingHKAuditMode(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/housekeeping/object#housekeeping

    Enable internal housekeeping for audit.
    """
    DISABLED = 0
    ENABLED = 1


class HousekeepingHKSessionsMode(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/housekeeping/object#housekeeping

    Enable internal housekeeping for sessions.
    """
    DISABLED = 0
    ENABLED = 1


class HousekeepingHKHistoryMode(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/housekeeping/object#housekeeping

    Enable internal housekeeping for history.
    """
    DISABLED = 0
    ENABLED = 1


class HousekeepingHKHistoryGlobal(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/housekeeping/object#housekeeping

    Override item history period.
    """
    NO = 0
    YES = 1


class HousekeepingHKTrendsMode(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/housekeeping/object#housekeeping

    Enable internal housekeeping for trends.
    """
    DISABLED = 0
    ENABLED = 1


class HousekeepingHKTrendsGlobal(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/housekeeping/object#housekeeping

    Override item trends period.
    """
    NO = 0
    YES = 1


class HousekeepingCompressionStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/housekeeping/object#housekeeping

    Enable TimescaleDB compression for history and trends.
    """
    OFF = 0
    ON = 1


class HousekeepingCompressionAvailability(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/housekeeping/object#housekeeping

    [Readonly]
    Compression availability.
    """
    UNAVAILABLE = 0
    AVAILABLE = 1
