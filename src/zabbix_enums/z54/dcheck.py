"""https://www.zabbix.com/documentation/5.4/en/manual/api/reference/dcheck/object"""
from zabbix_enums import _ZabbixEnum


class DiscoveryCheckSNMPv3AuthProtocol(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.4/en/manual/api/reference/dcheck/object#discovery-check

    Authentication protocol used for SNMPv3 agent checks with security level set to authNoPriv or authPriv.
    """
    MD5 = 0
    SHA = 1
    SHA1 = 1
    SHA224 = 2
    SHA256 = 3
    SHA384 = 4
    SHA512 = 5


class DiscoveryCheckSNMPv3PrivProtocol(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.4/en/manual/api/reference/dcheck/object#discovery-check

    Privacy protocol used for SNMPv3 agent checks with security level set to authPriv.
    """
    DES = 0
    AES = 1
    AES128 = 1
    AES192 = 2
    AES256 = 3
    AES192C = 4
    AES256C = 5



class DiscoveryCheckSNMPv3SecurityLevel(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.4/en/manual/api/reference/dcheck/object#discovery-check

    Security level used for SNMPv3 agent checks.
    """
    NOAUTHNOPRIV = 0
    AUTHNOPRIV = 1
    AUTHPRIV = 2


class DiscoveryCheckType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.4/en/manual/api/reference/dcheck/object#discovery-check

    Type of check.
    """
    SSH = 0
    LDAP = 1
    SMTP = 2
    FTP = 3
    HTTP = 4
    POP = 5
    NNTP = 6
    IMAP = 7
    TCP = 8
    ZABBIX_AGENT = 9
    SNMPV1 = 10
    SNMPV2 = 11
    ICMP = 12
    SNMPV3 = 13
    HTTPS = 14
    TELNET = 15


class DiscoveryCheckUniq(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.4/en/manual/api/reference/dcheck/object#discovery-check

    Whether to use this check as a device uniqueness criteria.
    Only a single unique check can be configured for a discovery rule.
    Used for Zabbix agent, SNMPv1, SNMPv2 and SNMPv3 agent checks.
    """
    NO = 0
    YES = 1


class DiscoveryCheckHostSource(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.4/en/manual/api/reference/dcheck/object#discovery-check

    Source for host name.
    """
    DNS = 1
    IP = 2
    CHECK_VALUE = 3


class DiscoveryCheckNameSource(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.4/en/manual/api/reference/dcheck/object#discovery-check

    Source for visible name.
    """
    NOT_SCPECIFIED = 0
    DNS = 1
    IP = 2
    CHECK_VALUE = 3
