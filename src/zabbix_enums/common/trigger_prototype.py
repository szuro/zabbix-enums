from .trigger import *
from . import _EntityStatus


class TriggerPrototypeFlag(IntEnum):
    PLAIN = 0
    DISCOVERED = 4


TriggerPrototypeStatus = _EntityStatus


class TriggerPrototypePriority(IntEnum):
    NOT_CLASSIFIED = 0
    INFORMATION = 1
    WARNING = 2
    AVERAGE = 3
    HIGH = 4
    DISASTER = 5


TriggerPrototypeState = TriggerState
TriggerPrototypeType = TriggerType
TriggerPrototypeValue = TriggerValue
TriggerPrototypeRecoveryMode = TriggerRecoveryMode
TriggerPrototypeCorrelationMode = TriggerCorrelationMode
TriggerPrototypeManualClose = TriggerManualClose
