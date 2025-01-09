"""https://www.zabbix.com/documentation/7.2/en/manual/api/reference/mfa/object"""
from zabbix_enums import _ZabbixEnum


class MFAType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.2/en/manual/api/reference/mfa/object#mfa
    
    Type of the MFA method.
    """
    TOPT = 1 
    DUO = 2


class MFAHashFunction(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.2/en/manual/api/reference/mfa/object#mfa
    
    Type of the hash function for generating TOTP codes.
    """
    SHA1 = 1
    SHA256 = 2
    SHA512 = 3

class MFACodeLength(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.2/en/manual/api/reference/mfa/object#mfa
    
    Verification code length.
    """
    SIX = 6
    EIGHT = 8
