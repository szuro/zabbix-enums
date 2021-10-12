from ._common_audit_log import AuditLogAction
from ._common_event import *
from ._common_host import *
from ._common_host_group import *
from ._common_host_interface import *
from ._common_item import *
from ._common_problem import *
from ._common_snmp import *
from ._common_trigger import *
from ._common_user_group import *


class ItemType(IntEnum):
    ZABBIX_AGENT = 0
    ZABBIX_TRAPPER = 2
    SIMPLE_CHECK = 3
    ZABBIX_INTERNAL = 5
    ZABBIX_AGENT_ACTIVE = 7
    ZABBIX_AGGREGATE = 8
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


class MacroType(IntEnum):
    TEXT = 0
    SECRET = 1


class AuditLogResourceType(IntEnum):
    USER = 0
    CONFIGURATION_OF_ZABBIX = 2
    MEDIA_TYPE = 3
    HOST = 4
    ACTION = 5
    GRAPH = 6
    GRAPH_ELEMENT = 7
    USER_GROUP = 11
    APPLICATION = 12
    TRIGGER = 13
    HOST_GROUP = 14
    ITEM = 15
    IMAGE = 16
    VALUE_MAP = 17
    SERVICE = 18
    MAP = 19
    SCREEN = 20
    WEB_SCENARIO = 22
    DISCOVERY_RULE = 23
    SLIDE_SHOW = 24
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
