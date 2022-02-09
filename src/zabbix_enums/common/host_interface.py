from enum import IntEnum


class HostInterfaceMain(IntEnum):
    NO = 0
    YES = 1


class HostIntrefaceUseIP(IntEnum):
    NO = 0
    YES = 1


class HostInterfaceType(IntEnum):
    AGENT = 1
    SNMP = 2
    IPMI = 3
    JMX = 4
