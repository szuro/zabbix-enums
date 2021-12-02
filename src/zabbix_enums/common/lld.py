from . import _EntityStatus, _NoYes, _YesNo, _Priority, _ZabbixEnum
from .item import ItemAuthTypeSSH
from .item_http import *
from .item_preprocessing import PreprocessingErrorHandler
from .host import HostInventoryMode


LLDStatus = _EntityStatus
LLDRuleAllowTraps = ItemAllowTraps
LLDRuleAuthTypeHTTP = ItemAuthTypeHTTP
LLDRuleAuthTypeSSH = ItemAuthTypeSSH
LLDRuleFollowRedirects = ItemFollowRedirects
LLDRuleOutputFormat = ItemOutputFormat
LLDRulePostType = ItemPostType
LLDRuleRequestMethod = ItemRequestMethod
LLDRuleRetrieveMode = ItemRetrieveMode
LLDRuleStatus = _EntityStatus
LLDRuleVerifyHost = ItemVerifyHost
LLDRuleVerifyPeer = ItemVerifyPeer



class LLDRuleEvalType(_ZabbixEnum):
    AND_OR = 0
    AND = 1
    OR = 2
    CUSTOM = 3


LLDRulePreprocessingErrorHandler = PreprocessingErrorHandler
LLDRuleOverridesStop = _NoYes
LLDRuleOverrideEvalType = LLDRuleEvalType
LLDRuleOverrideOperationDiscover = _YesNo
LLDRuleOverrideOperationSeverity = _Priority
LLDRuleOverrideOperationInventory = HostInventoryMode


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
