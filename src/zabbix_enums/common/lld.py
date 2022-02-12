from zabbix_enums.common import _ZabbixEnum


class LLDStatus(_ZabbixEnum):
    ENABLED = 0
    DISABLED = 1


class LLDRuleAllowTraps(_ZabbixEnum):
    NO = 0
    YES = 1


class LLDRuleAuthTypeHTTP(_ZabbixEnum):
    NONE = 0
    BASIC = 1
    NTLM = 2
    KERBEROS = 3


class LLDRuleAuthTypeSSH(_ZabbixEnum):
    PASSWORD = 0
    PUBLIC_KEY = 1


class LLDRuleFollowRedirects(_ZabbixEnum):
    NO = 0
    YES = 1


class LLDRuleOutputFormat(_ZabbixEnum):
    RAW = 0
    JSON = 1


class LLDRulePostType(_ZabbixEnum):
    RAW = 0
    JSON = 2
    XML = 3


class LLDRuleRequestMethod(_ZabbixEnum):
    GET = 0
    POST = 1
    PUT = 2
    HEAD  = 3


class LLDRuleRetrieveMode(_ZabbixEnum):
    BODY = 0
    HEADERS = 1
    BODY_AND_HEADERS = 2
    BOTH = 2


class LLDRuleStatus(_ZabbixEnum):
    ENABLED = 0
    DISABLED = 1


class LLDRuleVerifyHost(_ZabbixEnum):
    NO = 0
    YES = 1


class LLDRuleVerifyPeer(_ZabbixEnum):
    NO = 0
    YES = 1


class LLDRuleEvalType(_ZabbixEnum):
    AND_OR = 0
    AND = 1
    OR = 2
    CUSTOM = 3


class LLDRulePreprocessingErrorHandler(_ZabbixEnum):
    ERROR_MESSAGE = 0
    DISCARD_VALUE = 1
    CUSTOM_VALUE = 2
    CUSTOM_ERROR_MESSAGE = 3


class LLDRuleOverridesStop(_ZabbixEnum):
    NO = 0
    YES = 1


class LLDRuleOverrideEvalType(_ZabbixEnum):
    AND_OR = 0
    AND = 1
    OR = 2
    CUSTOM = 3


class LLDRuleOverrideOperationDiscover(_ZabbixEnum):
    YES = 0
    NO = 1


class LLDRuleOverrideOperationSeverity(_ZabbixEnum):
    NOT_CLASSIFIED = 0
    INFORMATION = 1
    WARNING = 2
    AVERAGE = 3
    HIGH = 4
    DISASTER = 5


class LLDRuleOverrideOperationInventory(_ZabbixEnum):
    DISABLED = -1
    MANUAL = 0
    AUTOMATIC = 1


class LLDRuleOverrideOperationObject(_ZabbixEnum):
    ITEM = 0
    TRIGGER = 1
    GRAPH = 2
    HOST = 3


class LLDRuleOverrideOperationOperator(_ZabbixEnum):
    EQUALS = 0
    DOES_NOT_EQUAL = 1
    CONTAINS = 2
    DOESN_NOT_CONTAIN = 3
    MATCHES = 8
    DOES_NOT_MATCH = 9


class LLDRuleOverrideOperationStatus(_ZabbixEnum):
    CREATE_ENABLED = 0
    CREATE_DISABLED = 1
