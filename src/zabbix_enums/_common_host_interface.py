from enum import IntEnum
from ._common import YesNo


HostInterfaceMain = YesNo
HostIntrefaceUseIP = YesNo


class HostInterfaceType(IntEnum):
    AGENT = 1
    SNMP = 2
    IPMI = 3
    JMX = 4
