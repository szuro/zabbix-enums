"""https://www.zabbix.com/documentation/7.2/en/manual/api/reference/itemprototype/object"""
from zabbix_enums import _ZabbixEnum


class ItemPrototypeType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.2/en/manual/api/reference/itemprototype/object#item-prototype

    Type of the item prototype.
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
    SNMP_TRAP = 17
    DEPENDENT_ITEM = 18
    HTTP_AGENT = 19
    SNMP_AGENT = 20
    SCRIPT = 21
    BROWSER = 22


class ItemPrototypeValueType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.2/en/manual/api/reference/itemprototype/object#item-prototype

    Type of information of the item prototype.
    """
    NUMERIC_FLOAT = 0
    CHARACTER = 1
    LOG = 2
    NUMERIC_UNSIGNED = 3
    TEXT = 4
    BINARY = 5


class ItemPrototypeAllowTraps(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.2/en/manual/api/reference/itemprototype/object#item-prototype

    HTTP agent item prototype field.
    Allow to populate value as in trapper item type also.
    """
    NO = 0
    YES = 1


class ItemPrototypeAuthTypeSSH(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.2/en/manual/api/reference/itemprototype/object#item-prototype


    Used only by SSH agent item prototypes or HTTP agent item prototypes.
    SSH agent authentication method possible values.
    """
    PASSWORD = 0
    PUBLIC_KEY = 1


class ItemPrototypeAuthTypeHTTP(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.2/en/manual/api/reference/itemprototype/object#item-prototype

    Used only by SSH agent item prototypes or HTTP agent item prototypes.
    HTTP agent authentication method possible values.
    """
    NONE = 0
    BASIC = 1
    NTLM = 2
    KERBEROS = 3


class ItemPrototypeFollowRedirects(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.2/en/manual/api/reference/itemprototype/object#item-prototype

    HTTP agent item prototype field.
    Follow response redirects while pooling data.
    """
    NO = 0
    YES = 1


class ItemPrototypeOutputFormat(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.2/en/manual/api/reference/itemprototype/object#item-prototype

    HTTP agent item prototype field.
    Should response be converted to JSON.
    """
    RAW = 0
    JSON = 1


class ItemPrototypePostType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.2/en/manual/api/reference/itemprototype/object#item-prototype

    HTTP agent item prototype field.
    Type of post data body stored in posts property.
    """
    RAW = 0
    JSON = 2
    XML = 3


class ItemPrototypeRequestMethod(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.2/en/manual/api/reference/itemprototype/object#item-prototype

    HTTP agent item prototype field.
    Type of request method.
    """
    GET = 0
    POST = 1
    PUT = 2
    HEAD = 3


class ItemPrototypeRetrieveMode(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.2/en/manual/api/reference/itemprototype/object#item-prototype

    HTTP agent item prototype field.
    What part of response should be stored.
    """
    BODY = 0
    HEADERS = 1
    BODY_AND_HEADERS = 2
    BOTH = 2


class ItemPrototypeStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.2/en/manual/api/reference/itemprototype/object#item-prototype

    Status of the item prototype.
    """
    ENABLED = 0
    DISABLED = 1
    UNSUPPORTED = 3


class ItemPrototypeVerifyHost(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.2/en/manual/api/reference/itemprototype/object#item-prototype

    HTTP agent item prototype field.
    Validate host name in URL is in Common Name field or a Subject Alternate Name field of host certificate.
    """
    NO = 0
    YES = 1


class ItemPrototypeVerifyPeer(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.2/en/manual/api/reference/itemprototype/object#item-prototype

    HTTP agent item prototype field.
    Validate is host certificate authentic.
    """
    NO = 0
    YES = 1


class ItemPrototypePrototypeDiscover(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.2/en/manual/api/reference/itemprototype/object#item-prototype-prototype

    Item prototype discovery status.
    """
    DISCOVER = 0
    DONT_DISCOVER = 1


class ItemPrototypePreprocessingType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.2/en/manual/api/reference/itemprototype/object#item-prototype-preprocessing

    The preprocessing option type.
    """
    CUSTOM_MULTIPLIER = 1
    RIGHT_TRIM = 2
    LEFT_TRIM = 3
    TRIM = 4
    REGULAR_EXPRESSION = 5
    BOOLEAN_TO_DECIMAL = 6
    OCTAL_TO_DECIMAL = 7
    HEXADECIMAL_TO_DECIMAL = 8
    SIMPLE_CHANGE = 9
    CHANGE_PER_SECOND = 10
    XML_XPATH = 11
    JSONPATH = 12
    IN_RANGE = 13
    MATCHES_REGULAR_EXPRESSION = 14
    DOES_NOT_MATCH_REGULAR_EXPRESSION = 15
    CHECK_FOR_ERROR_IN_JSON = 16
    CHECK_FOR_ERROR_IN_XML = 17
    CHECK_FOR_ERROR_USING_REGULAR_EXPRESSION = 18
    DISCARD_UNCHANGED = 19
    DISCARD_UNCHANGED_WITH_HEARTBEAT = 20
    JAVASCRIPT = 21
    PROMETHEUS_PATTERN = 22
    PROMETHEUS_TO_JSON = 23
    CSV_TO_JSON = 24
    REPLACE = 25
    CHECK_UNSUPPORTED = 26
    XML_TO_JSON = 27
    SNMP_WALK_VALUE = 28
    SNMP_WALK_TO_JSON = 29
    SNMP_GET_VALUE = 30


class ItemPrototypePreprocessingErrorHandler(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.2/en/manual/api/reference/itemprototype/object#item-prototype-preprocessing

    Action type used in case of preprocessing step failure.
    """
    ERROR_MESSAGE = 0
    DISCARD_VALUE = 1
    CUSTOM_VALUE = 2
    CUSTOM_ERROR_MESSAGE = 3
