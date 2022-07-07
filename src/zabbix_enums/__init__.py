from enum import IntEnum


class _ZabbixEnum(IntEnum):
    @classmethod
    def _missing_(cls, value):
        if isinstance(value, str):
            return cls(int(value))
