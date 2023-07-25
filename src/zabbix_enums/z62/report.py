"""https://www.zabbix.com/documentation/6.2/en/manual/api/reference/report/object"""
from zabbix_enums import _ZabbixEnum


class ReportPeriod(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/report/object#report

    Period for which the report will be prepared.
    """
    PREVIOUS_DAY = 0
    PREVIOUS_WEEK = 1
    PREVIOUS_MONTH = 2
    PREVIOUS_YEAR = 3


class ReportCycle(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/report/object#report

    Period repeating schedule.
    """
    DAILY = 0
    WEEKLY = 1
    MONTHLY = 2
    YEARLY = 3


class ReportStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/report/object#report

    Whether the report is enabled or disabled.
    """
    DISABLED = 0
    ENABLED = 1


class ReportState(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/report/object#report

    [Readonly]
    State of the report.
    """
    NOT_PROCESSED = 0
    GENERATED_AND_SENT = 1
    GENERATING_FAILED = 2
    GENERATED_AND_SENDING_FAILED = 3


class UsersExclude(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/report/object#users

    Whether to exclude the user from mailing list.
    """
    INCLUDE = 0
    EXCLUDE = 1
