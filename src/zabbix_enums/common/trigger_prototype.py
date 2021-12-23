from .trigger import *
from . import _EntityStatus, _Priority


class TriggerPrototypeFlag(IntEnum):
    PLAIN = 0
    DISCOVERED = 4


TriggerPrototypeStatus = _EntityStatus
TriggerPrototypePriority = _Priority
TriggerPrototypeState = TriggerState
TriggerPrototypeType = TriggerType
TriggerPrototypeValue = TriggerValue
TriggerPrototypeRecoveryMode = TriggerRecoveryMode
TriggerPrototypeCorrelationMode = TriggerCorrelationMode
TriggerPrototypeManualClose = TriggerManualClose
