from enum import IntEnum
from .._common import EntityStatus, NoYes, YesNo, Priority
from .item import ItemAuthTypeSSH
from .item_http import *
from .item_preprocessing import PreprocessingErrorHandler
from .host import HostInventoryMode


LLDStatus = EntityStatus
LLDRuleAllowTraps = ItemAllowTraps
LLDRuleAuthTypeHTTP = ItemAuthTypeHTTP
LLDRuleAuthTypeSSH = ItemAuthTypeSSH
LLDRuleFollowRedirects = ItemFollowRedirects
LLDRuleOutputFormat = ItemOutputFormat
LLDRulePostType = ItemPostType
LLDRuleRequestMethod = ItemRequestMethod
LLDRuleRetrieveMode = ItemRetrieveMode
LLDRuleStatus = EntityStatus
LLDRuleVerifyHost = ItemVerifyHost
LLDRuleVerifyPeer = ItemVerifyPeer


class LLDRuleType(IntEnum):
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


class LLDRuleEvalType(IntEnum):
    AND_OR = 0
    AND = 1
    OR = 2
    CUSTOM = 3


class LLDRuleOperator(IntEnum):
    MATCHES = 8
    DOES_NOT_MATCH = 9


class LLDRulePreprocessing(IntEnum):
    REGULAR_EXPRESSION = 5
    XML_XPATH = 11
    JSONPATH = 12
    DOES_NOT_MATCH_REGULAR_EXPRESSION = 15
    CHECK_FOR_ERROR_IN_JSON = 16
    CHECK_FOR_ERROR_IN_XML = 17
    DISCARD_UNCHANGED_WITH_HEARTBEAT = 20
    PROMETHEUS_PATTERN = 22
    PROMETHEUS_TO_JSON = 23
    CSV_TO_JSON = 24
    REPLACE = 25


LLDRulePreprocessingErrorHandler = PreprocessingErrorHandler
LLDRuleOverridesStop = NoYes
LLDRuleOverrideEvalType = LLDRuleEvalType
LLDRuleOverrideOperator = LLDRuleOperator
LLDRuleOverrideOperationDiscover = YesNo
LLDRuleOverrideOperationSeverity = Priority
LLDRuleOverrideOperationInventory = HostInventoryMode


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
