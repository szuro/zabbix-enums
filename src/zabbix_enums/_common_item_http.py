from enum import IntEnum
from ._common import NoYes


ItemAllowTraps = NoYes
ItemFollowRedirects = NoYes
ItemVerifyHost = NoYes
ItemVerifyPeer = NoYes


class ItemAuthTypeHTTP(IntEnum):
    NONE = 0
    BASIC = 1
    NTLM = 2
    KERBEROS = 3

class ItemOutputFormat(IntEnum):
    RAW = 0
    JSON = 1

class ItemPostType(IntEnum):
    RAW = 0
    JSON = 2
    XML = 3

class ItemRequestMethod(IntEnum):
    GET = 0
    POST = 1
    PUT = 2
    HEAD  = 3

class ItemRetrieveMode(IntEnum):
    BODY = 0
    HEADERS = 1
    BODY_AND_HEADERS = 2
    BOTH = 2
