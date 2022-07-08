"""https://www.zabbix.com/documentation/5.4/en/manual/api/reference/mediatype/object"""
from zabbix_enums import _ZabbixEnum


class MediaTypeType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.4/en/manual/api/reference/mediatype/object#media-type

    Transport used by the media type.
    """
    EMAIL = 0
    SCRIPT = 1
    SMS = 2
    WEBHOOK = 4


class MediaTypeSMTPSecurity(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.4/en/manual/api/reference/mediatype/object#media-type

    SMTP connection security level to use.
    """
    NONE = 0
    STARTTLS = 1
    SSL_TLS = 2


class MediaTypeSMTPSVerifyHost(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.4/en/manual/api/reference/mediatype/object#media-type

    SSL verify host for SMTP.
    """
    NO = 0
    YES = 1


class MediaTypeSMTPSVerifyPeer(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.4/en/manual/api/reference/mediatype/object#media-type

    SSL verify peer for SMTP.
    """
    NO = 0
    YES = 1


class MediaTypeSMTPAuthentication(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.4/en/manual/api/reference/mediatype/object#media-type

    SMTP authentication method to use.
    """
    NONE = 0
    PASSWORD = 1


class MediaTypeStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.4/en/manual/api/reference/mediatype/object#media-type

    Whether the media type is enabled.
    """
    ENABLED = 0
    DISABLED = 1


class MediaTypeContentType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.4/en/manual/api/reference/mediatype/object#media-type

    Message format.
    """
    PLAIN_TEXT = 0
    HTML = 1


class MediaTypeProcessTags(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.4/en/manual/api/reference/mediatype/object#media-type


    Defines should the webhook script response to be interpreted as tags and these tags should be added to associated event.
    """
    NO = 0
    YES = 1


class MediaTypeShowEventMenu(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.4/en/manual/api/reference/mediatype/object#media-type

    Show media type entry in problem.get and event.get property urls.
    """
    NO = 0
    YES = 1


class MessageTemplateEventSource(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.4/en/manual/api/reference/mediatype/object#message-template

    Event source.
    """
    TRIGGER = 0
    DISCOVERY = 1
    AUTOREGISTRATION = 2
    INTERNAL = 3


class MessageTemplateRecovery(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.4/en/manual/api/reference/mediatype/object#message-template

    Operation mode.
    """
    OPERATIONS = 0
    RECOVERY = 1
    RECOVERY_OPERATIONS = 1
    UPDATE = 2
    UPDATE_OPERATIONS = 2
