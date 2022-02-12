from zabbix_enums.common import _ZabbixEnum


class MediaTypeSMTPSVerifyHost(_ZabbixEnum):
    NO = 0
    YES = 1


class MediaTypeSMTPSVerifyPeer(_ZabbixEnum):
    NO = 0
    YES = 1


class MediaTypeStatus(_ZabbixEnum):
    ENABLED = 0
    DISABLED = 1


class MediaTypeProcessTags(_ZabbixEnum):
    NO = 0
    YES = 1


class MediaTypeShowEventMenu(_ZabbixEnum):
    NO = 0
    YES = 1


class MediaTypeEventSource(_ZabbixEnum):
    TRIGGER = 0
    DISCOVERY = 1
    AUTOREGISTRATION = 2
    INTERNAL = 3


class MediaType(_ZabbixEnum):
    EMAIL = 0
    SCRIPT = 1
    SMS = 2
    WEBHOOK = 4


class MediaTypeSMTPSecurity(_ZabbixEnum):
    NONE = 0
    STARTTLS = 1
    SSL_TLS = 2


class MediaTypeSMTPAuthentication(_ZabbixEnum):
    NONE = 0
    PASSWORD = 1


class MediaTypeContentType(_ZabbixEnum):
    PLAIN_TEXT = 0
    HTML = 1


class MediaTypeRecovery(_ZabbixEnum):
    OPERATIONS = 0
    RECOVERY = 1
    RECOVERY_OPERATIONS = 1
    UPDATE = 2
    UPDATE_OPERATIONS = 2
