from enum import IntEnum


class LLDStatus(IntEnum):
    ENABLED = 0
    DISABLED = 1


class LLDRuleAllowTraps(IntEnum):
    NO = 0
    YES = 1


class LLDRuleAuthTypeHTTP(IntEnum):
    NONE = 0
    BASIC = 1
    NTLM = 2
    KERBEROS = 3


class LLDRuleAuthTypeSSH(IntEnum):
    PASSWORD = 0
    PUBLIC_KEY = 1


class LLDRuleFollowRedirects(IntEnum):
    NO = 0
    YES = 1


class LLDRuleOutputFormat(IntEnum):
    RAW = 0
    JSON = 1


class LLDRulePostType(IntEnum):
    RAW = 0
    JSON = 2
    XML = 3


class LLDRuleRequestMethod(IntEnum):
    GET = 0
    POST = 1
    PUT = 2
    HEAD  = 3


class LLDRuleRetrieveMode(IntEnum):
    BODY = 0
    HEADERS = 1
    BODY_AND_HEADERS = 2
    BOTH = 2


class LLDRuleStatus(IntEnum):
    ENABLED = 0
    DISABLED = 1


class LLDRuleVerifyHost(IntEnum):
    NO = 0
    YES = 1


class LLDRuleVerifyPeer(IntEnum):
    NO = 0
    YES = 1


class LLDRuleEvalType(IntEnum):
    AND_OR = 0
    AND = 1
    OR = 2
    CUSTOM = 3


class LLDRulePreprocessingErrorHandler(IntEnum):
    ERROR_MESSAGE = 0
    DISCARD_VALUE = 1
    CUSTOM_VALUE = 2
    CUSTOM_ERROR_MESSAGE = 3


class LLDRuleOverridesStop(IntEnum):
    NO = 0
    YES = 1


class LLDRuleOverrideEvalType(IntEnum):
    AND_OR = 0
    AND = 1
    OR = 2
    CUSTOM = 3


class LLDRuleOverrideOperationDiscover(IntEnum):
    YES = 0
    NO = 1


class LLDRuleOverrideOperationSeverity(IntEnum):
    NOT_CLASSIFIED = 0
    INFORMATION = 1
    WARNING = 2
    AVERAGE = 3
    HIGH = 4
    DISASTER = 5


class LLDRuleOverrideOperationInventory(IntEnum):
    DISABLED = -1
    MANUAL = 0
    AUTOMATIC = 1


class LLDRuleOverrideOperationObject(IntEnum):
    ITEM = 0
    TRIGGER = 1
    GRAPH = 2
    HOST = 3


class LLDRuleOverrideOperationOperator(IntEnum):
    EQUALS = 0
    DOES_NOT_EQUAL = 1
    CONTAINS = 2
    DOESN_NOT_CONTAIN = 3
    MATCHES = 8
    DOES_NOT_MATCH = 9


class LLDRuleOverrideOperationStatus(IntEnum):
    CREATE_ENABLED = 0
    CREATE_DISABLED = 1
