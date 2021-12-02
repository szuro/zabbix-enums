from . import _ZabbixEnum


class AuditLogAction(_ZabbixEnum):
    ADD = 0
    UPDATE = 1
    DELETE = 2
    LOGIN = 3
    LOGOUT = 4
    ENABLE = 5
    DISABLE = 6
    EXECUTE = 7
