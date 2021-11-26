from enum import IntEnum
from .._common import NoYes


HostInterfaceMain = NoYes
HostIntrefaceUseIP = NoYes


class HostInterfaceType(IntEnum):
    AGENT = 1
    SNMP = 2
    IPMI = 3
    JMX = 4
