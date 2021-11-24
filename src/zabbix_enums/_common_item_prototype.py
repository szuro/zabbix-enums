from enum import IntEnum
from ._common import PrototypeDiscover


ItemPrototypeDiscover = PrototypeDiscover


class ItemPrototypeStatus(IntEnum):
    ENABLED = 0
    DISABLED = 1
    UNSUPPORTED = 3
