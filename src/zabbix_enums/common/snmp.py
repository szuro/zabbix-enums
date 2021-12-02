from . import _ZabbixEnum


class SNMPAuthProtocol(_ZabbixEnum):
    MD5 = 0
    SHA1 = 1
    SHA224 = 2
    SHA256 = 3
    SHA384 = 4
    SHA512 = 5


class SNMPPrivProtocol(_ZabbixEnum):
    DES = 0
    AES128 = 1
    AES192 = 2
    AES256 = 3
    AES192C = 4
    AES256C = 5
