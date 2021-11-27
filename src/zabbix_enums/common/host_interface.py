from enum import IntEnum
from . import _NoYes


HostInterfaceMain = _NoYes
HostIntrefaceUseIP = _NoYes


class HostInterfaceType(IntEnum):
    AGENT = 1
    SNMP = 2
    IPMI = 3
    JMX = 4
