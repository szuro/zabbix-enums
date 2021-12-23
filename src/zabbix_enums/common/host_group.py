from enum import IntEnum
from . import _DiscoveryFlag


HostGroupFlag = _DiscoveryFlag


class HostGroupInternal(IntEnum):
    NO = 0
    YES = 1
