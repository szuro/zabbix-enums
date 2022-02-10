from zabbix_enums.common import _ZabbixEnum
from .trigger import *


class TriggerPrototypeFlag(_ZabbixEnum):
    PLAIN = 0
    DISCOVERED = 4


TriggerPrototypeStatus = TriggerStatus
TriggerPrototypePriority = TriggerPriority
TriggerPrototypeState = TriggerState
TriggerPrototypeType = TriggerType
TriggerPrototypeValue = TriggerValue
TriggerPrototypeRecoveryMode = TriggerRecoveryMode
TriggerPrototypeCorrelationMode = TriggerCorrelationMode
TriggerPrototypeManualClose = TriggerManualClose
