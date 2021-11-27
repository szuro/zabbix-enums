from enum import IntEnum
from . import _PrototypeDiscover


ItemPrototypeDiscover = _PrototypeDiscover


class ItemPrototypeStatus(IntEnum):
    ENABLED = 0
    DISABLED = 1
    UNSUPPORTED = 3
