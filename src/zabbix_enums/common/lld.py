from enum import IntEnum
from . import _EntityStatus, _Priority
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



class LLDRuleEvalType(IntEnum):
    AND_OR = 0
    AND = 1
    OR = 2
    CUSTOM = 3


LLDRulePreprocessingErrorHandler = PreprocessingErrorHandler


class LLDRuleOverridesStop(IntEnum):
    NO = 0
    YES = 1


LLDRuleOverrideEvalType = LLDRuleEvalType


class LLDRuleOverrideOperationDiscover(IntEnum):
    YES = 0
    NO = 1


LLDRuleOverrideOperationSeverity = _Priority
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
