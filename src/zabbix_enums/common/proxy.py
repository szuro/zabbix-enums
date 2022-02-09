from enum import IntEnum


class ProxyStatus(IntEnum):
    ACTIVE = 5
    PASSIVE = 6


class ProxyType(IntEnum):
    ACTIVE = 5
    PASSIVE = 6


class ProxyUseIp(IntEnum):
    NO = 0
    YES = 1
