from . import _PrototypeDiscover, _ZabbixEnum


ItemPrototypeDiscover = _PrototypeDiscover


class ItemPrototypeStatus(_ZabbixEnum):
    ENABLED = 0
    DISABLED = 1
    UNSUPPORTED = 3
