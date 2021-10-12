from ._common import *
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
