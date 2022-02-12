from zabbix_enums.common import _ZabbixEnum


class DiscoveryCheckUniq(_ZabbixEnum):
    NO = 0
    YES = 1


class DiscoveryCheckType(_ZabbixEnum):
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


class DiscoveryCheckHostSource(_ZabbixEnum):
    DNS = 1
    IP = 2
    CHECK_VALUE = 3


class DiscoveryCheckNameSource(_ZabbixEnum):
    NOT_SCPECIFIED = 0
    DNS = 1
    IP = 2
    CHECK_VALUE = 3
