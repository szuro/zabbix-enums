from enum import IntEnum


class HostGroupFlag(IntEnum):
    PLAIN = 0
    DISCOVERED = 4


class HostGroupInternal(IntEnum):
    NO = 0
    YES = 1
