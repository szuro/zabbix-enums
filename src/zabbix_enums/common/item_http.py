from enum import IntEnum


class ItemAllowTraps(IntEnum):
    NO = 0
    YES = 1


class ItemFollowRedirects(IntEnum):
    NO = 0
    YES = 1


class ItemVerifyHost(IntEnum):
    NO = 0
    YES = 1


class ItemVerifyPeer(IntEnum):
    NO = 0
    YES = 1


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
