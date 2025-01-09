"""https://www.zabbix.com/documentation/7.2/en/manual/api/reference/auditlog/object"""
from zabbix_enums import _ZabbixEnum


class AuditLogAction(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.2/en/manual/api/reference/auditlog/object#audit-log

    Audit log entry action.
    """
    ADD = 0
    UPDATE = 1
    DELETE = 2
    LOGOUT = 4
    EXECUTE = 7
    LOGIN = 8
    FAILED_LOGIN = 9
    HISTORY_CLEAR = 10
    CONFIG_REFRESH = 11
    PUSH = 12


class AuditLogResourceType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.2/en/manual/api/reference/auditlog/object#audit-log

    Audit log entry resource type.
    """
    USER = 0
    MEDIA_TYPE = 3
    HOST = 4
    ACTION = 5
    GRAPH = 6
    USER_GROUP = 11
    TRIGGER = 13
    HOST_GROUP = 14
    ITEM = 15
    IMAGE = 16
    VALUE_MAP = 17
    SERVICE = 18
    MAP = 19
    WEB_SCENARIO = 22
    DISCOVERY_RULE = 23
    SCRIPT = 25
    PROXY = 26
    MAINTENANCE = 27
    REGULAR_EXPRESSION = 28
    MACRO = 29
    TEMPLATE = 30
    TRIGGER_PROTOTYPE = 31
    ICON_MAPPING = 32
    DASHBOARD = 33
    EVENT_CORRELATION = 34
    GRAPH_PROTOTYPE = 35
    ITEM_PROTOTYPE = 36
    HOST_PROTOTYPE = 37
    AUTOREGISTRATION = 38
    MODULE = 39
    SETTINGS = 40
    HOUSEKEEPING = 41
    AUTHENTICATION = 42
    DASHBOARD_TEMPLATE = 43
    TEMPLATE_DASHBOARD = 43
    USER_ROLE = 44
    AUTH_TOKEN = 45
    API_TOKEN = 45
    SCHEDULED_REPORT = 46
    HIGH_AVAILABILITY_NODE = 47
    SLA = 48
    LDAP_DIRECTORY = 49
    USER_DIRECTORY = 49
    TEMPLATE_GROUP = 50
    CONNECTOR = 51
    LLD_RULE = 52
    HISTORY = 53
