from enum import IntEnum
from . import _NoYes


class ProxyStatus(IntEnum):
    ACTIVE = 5
    PASSIVE = 6

ProxyType = ProxyStatus
ProxyUseIp = _NoYes
