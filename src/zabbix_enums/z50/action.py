"""https://www.zabbix.com/documentation/5.0/en/manual/api/reference/action/object"""
from zabbix_enums import _ZabbixEnum


class ActionStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/action/object#action

    Whether the action is enabled or disabled.
    """
    ENABLED = 0
    DISABLED = 1


class ActionPauseSupressed(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/action/object#action

    Whether to pause escalation during maintenance periods or not.
    """
    NO = 0
    YES = 1


class ActionOperationType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/action/object#action-operation

    Type of operation.
    """
    SEND_MESSAGE = 0
    REMOTE_COMMAND = 1
    ADD_HOST = 2
    REMOVE_HOST = 3
    ADD_TO_HOST_GROUP = 4
    REMOVE_FROM_HOST_GROUP = 5
    LINK_TO_TEMPLATE = 6
    UNLINK_FROM_TEMPLATE = 7
    ENABLE_HOST = 8
    DISABLE_HOST = 9
    SET_HOST_INVENTORY_MODE = 10


class ActionOperationEvalType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/action/object#action-operation

    Operation condition evaluation method.
    """
    AND_OR = 0
    AND = 1
    OR = 2


class ActionOperationCommandType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/action/object#action-operation-command

    Type of operation command.
    """
    CUSTOM_SCRIPT = 0
    IPMI = 1
    SSH = 2
    TELNET = 3
    GLOBAL_SCRIPT = 4


class ActionOperationCommandAuthType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/action/object#action-operation-command

    Authentication method used for SSH commands.
    """
    PASSWORD = 0
    PUBLIC_KEY = 1


class ActionOperationCommandExecuteOn(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/action/object#action-operation-command


    Target on which the custom script operation command will be executed.
    Required for custom script commands.
    """
    ZABBIX_AGENT = 0
    ZABBIX_SERVER = 1
    ZABBIX_SERVER_PROXY = 2


class ActionOperationMessageDefault(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/action/object#action-operation-message


    Whether to use the default action message text and subject.
    """
    NO = 0
    YES = 1


class ActionOperationConditionType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/action/object#action-operation-condition

    Type of condition.
    """

    EVENT_ACKNOWLEDGED = 14


class ActionOperationConditionOperator(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/action/object#action-operation-condition

    Condition operator.
    """
    EQUALS = 0


class ActionOperationConditionEventAcknowledged(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/action/object#action-operation-condition

    Whether the event is acknowledged.
    """
    NO = 0
    YES = 1


class ActionRecoveryOperationTypeTrigger(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/action/object#action-recovery-operation

    Type of operation.
    Possible values for trigger actions.
    """
    SEND_MESSAGE = 0
    REMOTE_COMMAND = 1
    NOTIFY_ALL_INVOLVED = 11


class ActionRecoveryOperationTypeInternal(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/action/object#action-recovery-operation

    Type of operation.
    Possible values for internal actions.
    """
    SEND_MESSAGE = 0
    NOTIFY_ALL_INVOLVED = 11


class ActionUpdateOperationTypeTrigger(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/action/object#action-update-operation

    Type of operation.
    Possible values for trigger actions.
    """
    SEND_MESSAGE = 0
    REMOTE_COMMAND = 1
    NOTIFY_ALL_INVOLVED = 12


class ActionFilterEvalType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/action/object#action-filter

    Filter condition evaluation method.
    """
    AND_OR = 0
    AND = 1
    OR = 2
    CUSTOM = 3


class ActionFilterCondidtionTypeTrigger(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/action/object#action-filter-condition

    Type of condition.
    Possible values for trigger actions.
    """
    HOST_GROUP = 0
    HOST = 1
    TRIGGER = 2
    TRIGGER_NAME = 3
    TRIGGER_SEVERITY = 4
    TIME_PERIOD = 6
    HOST_TEMPLATE = 13
    APPLICATION = 15
    PROBLEM_IS_SUPPRESSED = 16
    EVENT_TAG = 25
    EVENT_TAG_VALUE = 26


class ActionFilterCondidtionTypeDiscovery(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/action/object#action-filter-condition

    Type of condition.
    Possible values for discovery actions.
    """
    HOST_IP = 7
    DISCOVERED_SERVICE_TYPE = 8
    DISCOVERED_SERVICE_PORT = 9
    DISCOVERY_STATUS = 10
    UPTIME_OR_DOWNTIME_DURATION = 11
    RECEIVED_VALUE = 12
    DISCOVERY_RULE = 18
    DISCOVERY_CHECK = 19
    PROXY = 20
    DISCOVERY_OBJECT = 21


class ActionFilterCondidtionTypeAutoregistration(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/action/object#action-filter-condition

    Type of condition.
    Possible values for autoregistration actions.
    """
    PROXY = 20
    HOST_NAME = 22
    HOST_METADATA = 24


class ActionFilterCondidtionTypeInternal(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/action/object#action-filter-condition

    Type of condition.
    Possible values for internal actions.
    """
    HOST_GROUP = 0
    HOST = 1
    HOST_TEMPLATE = 13
    APPLICATION = 15
    EVENT_TYPE = 23


class ActionFilterCondidtionOperator(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/action/object#action-filter-condition

    Condition operator.
    """
    EQUALS = 0
    DOES_NOT_EQUAL = 1
    CONTAINS = 2
    DOES_NOT_CONTAIN = 3
    IN = 4
    GREATER_OR_EQUAL = 5
    LESS_OR_EQUAL = 6
    NOT_IN = 7
    MATCHES = 8
    DOES_NOT_MATCH = 9
    YES = 10
    NO = 11
