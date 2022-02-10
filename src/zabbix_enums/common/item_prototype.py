from zabbix_enums.common import _ZabbixEnum
from .item import ItemStatus

class ItemPrototypeDiscover(_ZabbixEnum):
    DISCOVER = 0
    DONT_DISCOVER = 1


ItemPrototypeStatus = ItemStatus
