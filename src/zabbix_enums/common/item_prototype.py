from enum import IntEnum
from .item import ItemStatus

class ItemPrototypeDiscover(IntEnum):
    DISCOVER = 0
    DONT_DISCOVER = 1


ItemPrototypeStatus = ItemStatus
