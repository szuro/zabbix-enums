from enum import IntEnum
from .host import HostStatus, HostInventoryMode


HostPrototypeStatus = HostStatus
HostPrototypeInventoryMode = HostInventoryMode


class HostPrototypeDiscover(IntEnum):
    DISCOVER = 0
    DONT_DISCOVER = 1
