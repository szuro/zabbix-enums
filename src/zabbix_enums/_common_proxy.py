from enum import IntEnum
from ._common import NoYes


class ProxyStatus(IntEnum):
    ACTIVE = 5
    PASSIVE = 6

ProxyType = ProxyStatus
ProxyUseIp = NoYes
