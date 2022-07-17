"""https://www.zabbix.com/documentation/6.0/en/manual/api/reference/service/object"""
from zabbix_enums import _ZabbixEnum


class ServiceAlgorithm(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.0/en/manual/api/reference/service/object#service

    Status calculation rule.
    Only applicable if child services exist.
    """

    SET_STATUS_TO_OK = 0
    MOST_CRITICAL_IF_ALL_CHILDREN_HAVE_PROBLEMS = 1
    MOST_CRITICAL_OF_CHILD_SERVICES = 2


class ServicePropagationRule(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.0/en/manual/api/reference/service/object#service

    Status propagation rule.
    Must be set together with propagation_value.

    PROPAGATE_SERVICE_STATUS_AS_IS - propagate service status as is - without any changes
    INCREASE_THE_STATUS - increase the propagated status by a given propagation_value (by 1 to 5 severities)
    DECREASE_THE_STATUS - decrease the propagated status by a given propagation_value (by 1 to 5 severities)
    IGNORE_THIS_SERVICE - ignore this service - the status is not propagated to the parent service at all
    SET_FIXED_SERVICE_STATUS - set fixed service status using a given propagation_value.
    """
    PROPAGATE_SERVICE_STATUS_AS_IS = 0
    INCREASE_THE_STATUS = 1
    DECREASE_THE_STATUS = 2
    IGNORE_THIS_SERVICE = 3
    SET_FIXED_SERVICE_STATUS = 4


class ServicePropagationValue(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.0/en/manual/api/reference/service/object#service

    Status propagation value. Must be set together with propagation_rule.
    """
    OK = -1
    NOT_CLASSIFIED = 0
    INFORMATION = 1
    WARNING = 2
    AVERAGE = 3
    HIGH = 4
    DISASTER = 5


class ServiceStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.0/en/manual/api/reference/service/object#service

    [Readonly]
    Whether the service is in OK or problem state.
    """
    OK = -1
    NOT_CLASSIFIED = 0
    INFORMATION = 1
    WARNING = 2
    AVERAGE = 3
    HIGH = 4
    DISASTER = 5


class ServiceReadOnly(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.0/en/manual/api/reference/service/object#service

    [Readonly]
    Access to the service.
    """
    READ_WRITE = 0
    READ_ONLY = 1


class StatusRuleType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.0/en/manual/api/reference/service/object#status-rule

    Condition for setting (New status) status.

    AT_LEAST_N_CHILD_SERVICES_WITH_STATUS_OR_ABOVE - if at least (N) child services have (Status) status or above
    AT_LEAST_NP_CHILD_SERVICES_WITH_STATUS_OR_ABOVE - if at least (N%) of child services have (Status) status or above
    LESS_THAN_N_CHILD_SERVICES_WITH_STATUS_OR_BELOW - if less than (N) child services have (Status) status or below
    LESS_THAN_NP_CHILD_SERVICES_WITH_STATUS_OR_BELOW - if less than (N%) of child services have (Status) status or below
    CHILD_SERVICE_WEIGHT_WITH_STATUS_OR_ABOVE_AT_LEAST_W - if weight of child services with (Status) status or above is at least (W)
    CHILD_SERVICE_WEIGHT_WITH_STATUS_OR_ABOVE_AT_LEAST_NP - if weight of child services with (Status) status or above is at least (N%)
    CHILD_SERVICE_WEIGHT_WITH_STATUS_OR_BELOW_AT_MOST_W - if weight of child services with (Status) status or below is less than (W)
    CHILD_SERVICE_WEIGHT_WITH_STATUS_OR_BELOW_AT_MOST_NP - if weight of child services with (Status) status or below is less than (N%)

    Where:
    - N (W) is limit_value
    - (Status) is limit_status
    - (New status) is new_status
    """
    AT_LEAST_N_CHILD_SERVICES_WITH_STATUS_OR_ABOVE = 0
    AT_LEAST_NP_CHILD_SERVICES_WITH_STATUS_OR_ABOVE = 1
    LESS_THAN_N_CHILD_SERVICES_WITH_STATUS_OR_BELOW = 2
    LESS_THAN_NP_CHILD_SERVICES_WITH_STATUS_OR_BELOW = 3
    CHILD_SERVICE_WEIGHT_WITH_STATUS_OR_ABOVE_AT_LEAST_W = 4
    CHILD_SERVICE_WEIGHT_WITH_STATUS_OR_ABOVE_AT_LEAST_NP = 5
    CHILD_SERVICE_WEIGHT_WITH_STATUS_OR_BELOW_AT_MOST_W = 6
    CHILD_SERVICE_WEIGHT_WITH_STATUS_OR_BELOW_AT_MOST_NP = 7


class StatusRuleLimitStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.0/en/manual/api/reference/service/object#status-rule

    Limit status.
    """
    OK = -1
    NOT_CLASSIFIED = 0
    INFORMATION = 1
    WARNING = 2
    AVERAGE = 3
    HIGH = 4
    DISASTER = 5


class StatusRuleLimitStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.0/en/manual/api/reference/service/object#status-rule

    New status value.
    """
    NOT_CLASSIFIED = 0
    INFORMATION = 1
    WARNING = 2
    AVERAGE = 3
    HIGH = 4
    DISASTER = 5


class ProblemTagOperator(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.0/en/manual/api/reference/service/object#problem-tag

    Mapping condition operator.
    """
    EQUALS = 0
    LIKE = 2
