from . import _NoYes, _ZabbixEnum


ItemAllowTraps = _NoYes
ItemFollowRedirects = _NoYes
ItemVerifyHost = _NoYes
ItemVerifyPeer = _NoYes


class ItemAuthTypeHTTP(_ZabbixEnum):
    NONE = 0
    BASIC = 1
    NTLM = 2
    KERBEROS = 3

class ItemOutputFormat(_ZabbixEnum):
    RAW = 0
    JSON = 1

class ItemPostType(_ZabbixEnum):
    RAW = 0
    JSON = 2
    XML = 3

class ItemRequestMethod(_ZabbixEnum):
    GET = 0
    POST = 1
    PUT = 2
    HEAD  = 3

class ItemRetrieveMode(_ZabbixEnum):
    BODY = 0
    HEADERS = 1
    BODY_AND_HEADERS = 2
    BOTH = 2
