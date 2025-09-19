"""https://www.zabbix.com/documentation/7.4/en/manual/api/reference/discoveryruleprototype/object"""
from zabbix_enums import _ZabbixEnum

class LLDRulePrototypeType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/discoveryruleprototype/object#lld-rule-prototype-object

    Type of the LLD rule prototype.
    """
    ZABBIX_AGENT = 0
    ZABBIX_TRAPPER = 2
    SIMPLE_CHECK = 3
    ZABBIX_INTERNAL = 5
    ZABBIX_AGENT_ACTIVE = 7
    WEB_ITEM = 9
    EXTERNAL_CHECK = 10
    DATABASE_MONITOR = 11
    IPMI_AGENT = 12
    SSH_AGENT = 13
    TELNET_AGENT = 14
    CALCULATED = 15
    JMX_AGENT = 16
    SNMP_TRAP = 17
    DEPENDENT_ITEM = 18
    HTTP_AGENT = 19
    SNMP_AGENT = 20
    SCRIPT = 21
    BROWSER = 22
    NESTED = 23


class LLDRulePrototypeAuthTypeSSH(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/discoveryruleprototype/object#lld-rule-prototype-object

    Authentication method.
    """
    PASSWORD = 0
    PUBLIC_KEY = 1


class LLDRulePrototypeAuthTypeHTTP(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/discoveryruleprototype/object#lld-rule-prototype-object
    
    Authentication method.
    """
    NONE = 0
    BASIC = 1
    NTLM = 2
    KERBEROS = 3



class LLDRulePrototypeFollowRedirects(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/discoveryruleprototype/object#lld-rule-prototype-object

    Follow response redirects while polling data.
    """
    NO = 0
    YES = 1


class LLDRulePrototypeLifetimeType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/discoveryruleprototype/object#lld-rule-prototype-object

    Scenario to delete lost LLD resources.
    """
    DELETE_AFTER_LIFETIME = 0
    DO_NOT_DELETE = 1
    DELETE_IMMEDIATELY = 2


class LLDRulePrototypeEnabledLifetimeType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/discoveryruleprototype/object#lld-rule-prototype-object
    
    Scenario to disable lost LLD resources.
    """
    DISABLE_AFTER_LIFETIME = 0
    DO_NOT_DISABLE = 1
    DISABLE_IMMEDIATELY = 2


class LLDRulePrototypeOutputFormat(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/discoveryruleprototype/object#lld-rule-prototype-object

    Should response be converted to JSON.
    """
    RAW = 0
    JSON = 1


class LLDRulePrototypePostType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/discoveryruleprototype/object#lld-rule-prototype-object 

    Type of post data body stored in posts property.
    """
    RAW = 0
    JSON = 2
    XML = 3




class LLDRulePrototypeRequestMethod(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/discoveryruleprototype/object#lld-rule-prototype-object

    Type of request method.
    """
    GET = 0
    POST = 1
    PUT = 2
    HEAD = 3



class LLDRulePrototypeRetrieveMode(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/discoveryruleprototype/object#lld-rule-prototype-object

    What part of response should be stored.
    """
    BODY = 0
    HEADERS = 1
    BODY_AND_HEADERS = 2


class LLDRulePrototypeState(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/discoveryruleprototype/object#lld-rule-prototype-object

    [Readonly]
    State of the item.
    """
    NORMAL = 0
    NOT_SUPPORTED = 1


class LLDRulePrototypeStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/discoveryruleprototype/object#lld-rule-prototype-object

    Status of the item.
    """
    ENABLED = 0
    DISABLED = 1



class LLDRulePrototypeVerifyHost(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/discoveryruleprototype/object#lld-rule-prototype-object

    Validate host name in URL is in Common Name field or a Subject Alternate Name field of host certificate.
    """
    NO = 0
    YES = 1


class LLDRulePrototypeVerifyPeer(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/discoveryruleprototype/object#lld-rule-prototype-object

    Validate is host certificate authentic.
    """
    NO = 0
    YES = 1


class LLDRulePrototypeEvalType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/discoveryruleprototype/object#lld-rule-prototype-object

    Filter condition evaluation method.
    """
    AND_OR = 0
    AND = 1
    OR = 2
    CUSTOM = 3

class LLDRulePrototypeFilterConditionOperator(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/discoveryruleprototype/object#lld-rule-filter-condition

    Condition operator.
    """
    MATCHES_REGEX = 8
    DOES_NOT_MATCH_REGEX = 9
    EXISTS = 12
    DOES_NOT_EXIST = 13


class LLDRulePrototypePreprocessing(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/discoveryruleprototype/object#lld-rule-preprocessing

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


class LLDRulePrototypePreprocessingErrorHandler(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/discoveryruleprototype/object#lld-rule-preprocessing

    Action type used in case of preprocessing step failure.
    """
    ERROR_MESSAGE = 0
    DISCARD_VALUE = 1
    CUSTOM_VALUE = 2
    CUSTOM_ERROR_MESSAGE = 3


class LLDRulePrototypeOverridesStop(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/discoveryruleprototype/object#lld-rule-overrides

    Stop processing next overrides if matches.
    """
    NO = 0
    YES = 1


class LLDRulePrototypeOverrideFilterEvalType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/discoveryruleprototype/object#lld-rule-override-filter

    Override filter condition evaluation method.
    """
    AND_OR = 0
    AND = 1
    OR = 2
    CUSTOM = 3


class LLDRulePrototypeOverrideFilterConditionOperator(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/discoveryruleprototype/object#lld-rule-override-filter-condition

    Condition operator.
    """
    MATCHES_REGEX = 8
    DOES_NOT_MATCH_REGEX = 9
    EXISTS = 12
    DOES_NOT_EXIST = 13


class LLDRulePrototypeOverrideOperationObject(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/discoveryruleprototype/object#lld-rule-override-operation

    Type of discovered object to perform the action.
    """
    ITEM = 0
    TRIGGER = 1
    GRAPH = 2
    HOST = 3


class LLDRulePrototypeOverrideOperationOperator(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/discoveryruleprototype/object#lld-rule-override-operation

    Override condition operator.
    """
    EQUALS = 0
    DOES_NOT_EQUAL = 1
    CONTAINS = 2
    DOESN_NOT_CONTAIN = 3
    MATCHES = 8
    DOES_NOT_MATCH = 9


class LLDRulePrototypeOverrideOperationStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/discoveryruleprototype/object#lld-rule-override-operation-status

    Override the status for selected object.
    """
    CREATE_ENABLED = 0
    CREATE_DISABLED = 1


class LLDRulePrototypeOverrideOperationDiscover(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/discoveryruleprototype/object#lld-rule-override-operation-discover

    Override the discover status for selected object.
    """
    YES = 0
    NO = 1


class LLDRulePrototypeOverrideOperationSeverity(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/discoveryruleprototype/object#lld-rule-override-operation-severity

    Override the severity of trigger prototype.
    """
    NOT_CLASSIFIED = 0
    INFORMATION = 1
    WARNING = 2
    AVERAGE = 3
    HIGH = 4
    DISASTER = 5


class LLDRulePrototypeOverrideOperationInventory(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/discoveryruleprototype/object#lld-rule-override-operation-inventory

    Override the host prototype inventory mode.
    """
    DISABLED = -1
    MANUAL = 0
    AUTOMATIC = 1
