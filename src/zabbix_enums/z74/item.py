"""https://www.zabbix.com/documentation/7.4/en/manual/api/reference/item/object"""
from zabbix_enums import _ZabbixEnum


class ItemType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/item/object#item

    Type of the item.
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


class ItemValueType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/item/object#item

    Type of information of the item.
    """
    NUMERIC_FLOAT = 0
    CHARACTER = 1
    LOG = 2
    NUMERIC_UNSIGNED = 3
    TEXT = 4
    BINARY = 5


class ItemAllowTraps(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/item/object#item

    HTTP agent item field.
    Allow to populate value as in trapper item type also.
    """
    NO = 0
    YES = 1


class ItemAuthTypeSSH(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/item/object#item


    Used only by SSH agent items or HTTP agent items.
    SSH agent authentication method possible values.
    """
    PASSWORD = 0
    PUBLIC_KEY = 1


class ItemAuthTypeHTTP(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/item/object#item

    Used only by SSH agent items or HTTP agent items.
    HTTP agent authentication method possible values.
    """
    NONE = 0
    BASIC = 1
    NTLM = 2
    KERBEROS = 3


class ItemFlag(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/item/object#item

    [Readonly]
    Origin of the item.
    """
    PLAIN = 0
    DISCOVERED = 4


class ItemFollowRedirects(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/item/object#item

    HTTP agent item field.
    Follow response redirects while pooling data.
    """
    NO = 0
    YES = 1


class ItemOutputFormat(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/item/object#item

    HTTP agent item field.
    Should response be converted to JSON.
    """
    RAW = 0
    JSON = 1


class ItemPostType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/item/object#item

    HTTP agent item field.
    Type of post data body stored in posts property.
    """
    RAW = 0
    JSON = 2
    XML = 3


class ItemRequestMethod(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/item/object#item

    HTTP agent item field.
    Type of request method.
    """
    GET = 0
    POST = 1
    PUT = 2
    HEAD = 3


class ItemRetrieveMode(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/item/object#item

    HTTP agent item field.
    What part of response should be stored.
    """
    BODY = 0
    HEADERS = 1
    BODY_AND_HEADERS = 2
    BOTH = 2


class ItemState(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/item/object#item

    [Readonly]
    State of the item.
    """
    NORMAL = 0
    NOT_SUPPORTED = 1


class ItemStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/item/object#item

    Status of the item.
    """
    ENABLED = 0
    DISABLED = 1


class ItemVerifyHost(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/item/object#item

    HTTP agent item field.
    Validate host name in URL is in Common Name field or a Subject Alternate Name field of host certificate.
    """
    NO = 0
    YES = 1


class ItemVerifyPeer(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/item/object#item

    HTTP agent item field.
    Validate is host certificate authentic.
    """
    NO = 0
    YES = 1


class ItemPreprocessingType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/item/object#item-preprocessing

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


class ItemPreprocessingErrorHandler(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/item/object#item-preprocessing

    Action type used in case of preprocessing step failure.
    """
    ERROR_MESSAGE = 0
    DISCARD_VALUE = 1
    CUSTOM_VALUE = 2
    CUSTOM_ERROR_MESSAGE = 3
