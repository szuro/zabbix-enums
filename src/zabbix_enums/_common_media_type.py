from enum import IntEnum
from ._common import NoYes, EntityStatus, ObjectSource


MediaTypeSMTPSVerifyHost = NoYes
MediaTypeSMTPSVerifyPeer = NoYes
MediaTypeStatus = EntityStatus
MediaTypeProcessTags = NoYes
MediaTypeShowEventMenu = NoYes
MediaTypeEventSource = ObjectSource


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
