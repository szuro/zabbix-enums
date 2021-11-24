from enum import IntEnum
from ._common import YesNo


class ProxyStatus(IntEnum):
    ACTIVE = 5
    PASSIVE = 6

ProxyType = ProxyStatus
ProxyUseIp = YesNo
