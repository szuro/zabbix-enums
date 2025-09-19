"""https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/object"""
from zabbix_enums import _ZabbixEnum


class LLDRuleType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/object#lld-rule

    Type of the LLD rule.
    """
    ZABBIX_AGENT = 0
    ZABBIX_TRAPPER = 2
    SIMPLE_CHECK = 3
    ZABBIX_INTERNAL = 5
    ZABBIX_AGENT_ACTIVE = 7
    EXTERNAL_CHECK = 10
    DATABASE_MONITOR = 11
    IPMI_AGENT = 12
    SSH_AGENT = 13
    TELNET_AGENT = 14
    CALCULATED = 15
    JMX_AGENT = 16
    DEPENDENT_ITEM = 18
    HTTP_AGENT = 19
    SNMP_AGENT = 20
    SCRIPT = 21
    BROWSER = 22


class LLDRuleAllowTraps(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/object#lld-rule

    HTTP agent LLD rule field. Allow to populate value as in trapper item type also.
    """
    NO = 0
    YES = 1


class LLDRuleAuthTypeSSH(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/object#lld-rule

    Used only by SSH agent or HTTP agent LLD rules.
    SSH agent authentication method possible values.
    """
    PASSWORD = 0
    PUBLIC_KEY = 1


class LLDRuleAuthTypeHTTP(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/object#lld-rule

    Used only by SSH agent or HTTP agent LLD rules.
    HTTP agent authentication method possible values.
    """
    NONE = 0
    BASIC = 1
    NTLM = 2


class LLDRuleFollowRedirects(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/object#lld-rule

    HTTP agent LLD rule field.
    Follow response redirects while pooling data.
    """
    NO = 0
    YES = 1


class LLDRuleLifetimeType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/object#lld-rule

    Scenario to delete lost LLD resources.
    """
    DELETE_AFTER_THRESHOLD = 0
    DO_NOT_DELETE = 1
    DELETE_IMMEDIATELY = 2


class LLDRuleEnabledLifetimeType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/object#lld-rule

    Scenario to disable lost LLD resources.
    """
    DISABLE_AFTER_THRESHOLD = 0
    DO_NOT_DISABLE = 1
    DISABLE_IMMEDIATELY = 2


class LLDRuleOutputFormat(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/object#lld-rule

    HTTP agent LLD rule field.
    Should response be converted to JSON.
    """
    RAW = 0
    JSON = 1


class LLDRulePostType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/object#lld-rule

    HTTP agent LLD rule field.
    Type of post data body stored in posts property.
    """
    RAW = 0
    JSON = 2
    XML = 3


class LLDRuleRequestMethod(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/object#lld-rule

    HTTP agent LLD rule field.
    Type of request method.
    """
    GET = 0
    POST = 1
    PUT = 2
    HEAD = 3


class LLDRuleRetrieveMode(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/object#lld-rule

    HTTP agent LLD rule field.
    What part of response should be stored.
    """
    BODY = 0
    HEADERS = 1
    BODY_AND_HEADERS = 2
    BOTH = 2


class LLDRuleState(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/object#lld-rule

    [Readonly]
    State of the LLD rule.
    """
    NORMAL = 0
    NOT_SUPPORTED = 1


class LLDRuleStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/object#lld-rule

    Status of the LLD rule.
    """
    ENABLED = 0
    DISABLED = 1


class LLDRuleVerifyHost(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/object#lld-rule

    HTTP agent LLD rule field.
    Validate host name in URL is in Common Name field or a Subject Alternate Name field of host certificate.
    """
    NO = 0
    YES = 1


class LLDRuleVerifyPeer(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/object#lld-rule

    HTTP agent LLD rule field.
    Validate is host certificate authentic.
    """
    NO = 0
    YES = 1


class LLDRuleEvalType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/object#lld-rule-filter

    Filter condition evaluation method.
    """
    AND_OR = 0
    AND = 1
    OR = 2
    CUSTOM = 3


class LLDRuleFilterConditionOperator(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/object#lld-rule-filter-condition

    Condition operator.
    """
    MATCHES_REGEX = 8
    DOES_NOT_MATCH_REGEX = 9
    EXISTS = 12
    DOES_NOT_EXIST = 13


class LLDRulePreprocessing(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/object#lld-rule-preprocessing

    The preprocessing option type.
    """
    REGULAR_EXPRESSION = 5
    XML_XPATH = 11
    JSONPATH = 12
    MATCHES_REGULAR_EXPRESSION = 14
    DOES_NOT_MATCH_REGULAR_EXPRESSION = 15
    CHECK_FOR_ERROR_IN_JSON = 16
    CHECK_FOR_ERROR_IN_XML = 17
    DISCARD_UNCHANGED_WITH_HEARTBEAT = 20
    JAVASCRIPT = 21
    PROMETHEUS_TO_JSON = 23
    CSV_TO_JSON = 24
    REPLACE = 25
    XML_TO_JSON = 27
    SNMP_WALK_VALUE = 28
    SNMP_WALK_TO_JSON = 29
    SNMP_GET_VALUE = 30


class LLDRulePreprocessingErrorHandler(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/object#lld-rule-preprocessing

    Action type used in case of preprocessing step failure.
    """
    ERROR_MESSAGE = 0
    DISCARD_VALUE = 1
    CUSTOM_VALUE = 2
    CUSTOM_ERROR_MESSAGE = 3


class LLDRuleOverridesStop(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/object#lld-rule-overrides

    Stop processing next overrides if matches.
    """
    NO = 0
    YES = 1


class LLDRuleOverrideFilterEvalType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/object#lld-rule-override-filter

    Override filter condition evaluation method.
    """
    AND_OR = 0
    AND = 1
    OR = 2
    CUSTOM = 3


class LLDRuleOverrideFilterConditionOperator(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/object#lld-rule-override-filter-condition

    Condition operator.
    """
    MATCHES_REGEX = 8
    DOES_NOT_MATCH_REGEX = 9
    EXISTS = 12
    DOES_NOT_EXIST = 13


class LLDRuleOverrideOperationObject(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/object#lld-rule-override-operation

    Type of discovered object to perform the action.
    """
    ITEM = 0
    TRIGGER = 1
    GRAPH = 2
    HOST = 3


class LLDRuleOverrideOperationOperator(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/object#lld-rule-override-operation

    Override condition operator.
    """
    EQUALS = 0
    DOES_NOT_EQUAL = 1
    CONTAINS = 2
    DOESN_NOT_CONTAIN = 3
    MATCHES = 8
    DOES_NOT_MATCH = 9


class LLDRuleOverrideOperationStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/object#lld-rule-override-operation-status

    Override the status for selected object.
    """
    CREATE_ENABLED = 0
    CREATE_DISABLED = 1


class LLDRuleOverrideOperationDiscover(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/object#lld-rule-override-operation-discover

    Override the discover status for selected object.
    """
    YES = 0
    NO = 1


class LLDRuleOverrideOperationSeverity(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/object#lld-rule-override-operation-severity

    Override the severity of trigger prototype.
    """
    NOT_CLASSIFIED = 0
    INFORMATION = 1
    WARNING = 2
    AVERAGE = 3
    HIGH = 4
    DISASTER = 5


class LLDRuleOverrideOperationInventory(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/discoveryrule/object#lld-rule-override-operation-inventory

    Override the host prototype inventory mode.
    """
    DISABLED = -1
    MANUAL = 0
    AUTOMATIC = 1
