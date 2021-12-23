from enum import IntEnum


class MediaTypeSMTPSVerifyHost(IntEnum):
    NO = 0
    YES = 1


class MediaTypeSMTPSVerifyPeer(IntEnum):
    NO = 0
    YES = 1


class MediaTypeStatus(IntEnum):
    ENABLED = 0
    DISABLED = 1


class MediaTypeProcessTags(IntEnum):
    NO = 0
    YES = 1


class MediaTypeShowEventMenu(IntEnum):
    NO = 0
    YES = 1


class MediaTypeEventSource(IntEnum):
    TRIGGER = 0
    DISCOVERY = 1
    AUTOREGISTRATION = 2
    INTERNAL = 3


class MediaType(IntEnum):
    EMAIL = 0
    SCRIPT = 1
    SMS = 2
    WEBHOOK = 4


class MediaTypeSMTPSecurity(IntEnum):
    NONE = 0
    STARTTLS = 1
    SSL_TLS = 2


class MediaTypeSMTPAuthentication(IntEnum):
    NONE = 0
    PASSWORD = 1


class MediaTypeContentType(IntEnum):
    PLAIN_TEXT = 0
    HTML = 1


class MediaTypeRecovery(IntEnum):
    OPERATIONS = 0
    RECOVERY = 1
    RECOVERY_OPERATIONS = 1
    UPDATE = 2
    UPDATE_OPERATIONS = 2
