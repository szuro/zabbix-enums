"""https://www.zabbix.com/documentation/5.0/en/manual/api/reference/triggerprototype/object"""
from zabbix_enums import _ZabbixEnum


class TriggerPrototypePriority(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/triggerprototype/object#trigger-prototype

    Severity of the trigger prototype.
    """
    NOT_CLASSIFIED = 0
    INFORMATION = 1
    WARNING = 2
    AVERAGE = 3
    HIGH = 4
    DISASTER = 5


class TriggerPrototypeStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/triggerprototype/object#trigger-prototype

    Whether the trigger prototype is enabled or disabled.
    """
    ENABLED = 0
    DISABLED = 1


class TriggerPrototypeType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/triggerprototype/object#trigger-prototype

    Whether the trigger can generate multiple problem events.
    """
    GENERATE_SINGLE_EVENT = 0
    DO_NOT_GENERATE_MULTIPLE_EVENTS = 0
    GENERATE_MULTIPLE_EVENTS = 1


class TriggerPrototypeRecoveryMode(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/triggerprototype/object#trigger-prototype

    OK event generation mode.
    """
    EXPRESSION = 0
    RECOVERY_EXPRESSION = 1
    NONE = 2


class TriggerPrototypeCorrelationMode(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/triggerprototype/object#trigger-prototype

    OK event closes. 
    """
    ALL_PROBLEMS = 0
    TAG_VALUES_MATCH = 1


class TriggerPrototypeManualClose(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/triggerprototype/object#trigger-prototype

    Allow manual close.
    """
    NO = 0
    YES = 1


class TriggerPrototypeDiscover(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/triggerprototype/object#trigger-prototype

    Trigger prototype discovery status.
    """
    DISCOVER = 0
    DONT_DISCOVER = 1
