from zabbix_enums.common import _ZabbixEnum
from .host import HostStatus, HostInventoryMode


HostPrototypeStatus = HostStatus
HostPrototypeInventoryMode = HostInventoryMode


class HostPrototypeDiscover(_ZabbixEnum):
    DISCOVER = 0
    DONT_DISCOVER = 1
