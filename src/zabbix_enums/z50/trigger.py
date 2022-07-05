"""https://www.zabbix.com/documentation/5.0/en/manual/api/reference/trigger/object"""
from zabbix_enums import _ZabbixEnum


class TriggerFlag(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/trigger/object#trigger

    [Readonly]
    Origin of the trigger.
    """
    PLAIN = 0
    DISCOVERED = 4


class TriggerPriority(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/trigger/object#trigger

    Severity of the trigger.
    """
    NOT_CLASSIFIED = 0
    INFORMATION = 1
    WARNING = 2
    AVERAGE = 3
    HIGH = 4
    DISASTER = 5


class TriggerState(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/trigger/object#trigger

    [Readonly]
    State of the trigger.
    """
    NORMAL = 0
    UNKNOWN = 1


class TriggerStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/trigger/object#trigger

    Whether the trigger is enabled or disabled.
    """
    ENABLED = 0
    DISABLED = 1


class TriggerType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/trigger/object#trigger

    Whether the trigger can generate multiple problem events.
    """
    GENERATE_SINGLE_EVENT = 0
    DO_NOT_GENERATE_MULTIPLE_EVENTS = 0
    GENERATE_MULTIPLE_EVENTS = 1


class TriggerValue(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/trigger/object#trigger

    [Readonly]
    Whether the trigger is in OK or problem state.
    """
    OK = 0
    PROBLEM = 1


class TriggerRecoveryMode(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/trigger/object#trigger

    OK event generation mode.
    """
    EXPRESSION = 0
    RECOVERY_EXPRESSION = 1
    NONE = 2


class TriggerCorrelationMode(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/trigger/object#trigger

    OK event closes. 
    """
    ALL_PROBLEMS = 0
    TAG_VALUES_MATCH = 1


class TriggerManualClose(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/trigger/object#trigger

    Allow manual close.
    """
    NO = 0
    YES = 1
