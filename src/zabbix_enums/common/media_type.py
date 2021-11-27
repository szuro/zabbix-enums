from enum import IntEnum
from . import _NoYes, _EntityStatus, _ObjectSource


MediaTypeSMTPSVerifyHost = _NoYes
MediaTypeSMTPSVerifyPeer = _NoYes
MediaTypeStatus = _EntityStatus
MediaTypeProcessTags = _NoYes
MediaTypeShowEventMenu = _NoYes
MediaTypeEventSource = _ObjectSource


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
