from enum import IntEnum


class ProxyStatus(IntEnum):
    ACTIVE = 5
    PASSIVE = 6

ProxyType = ProxyStatus


class ProxyUseIp(IntEnum):
    NO = 0
    YES = 1
