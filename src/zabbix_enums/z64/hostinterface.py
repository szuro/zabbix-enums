"""https://www.zabbix.com/documentation/6.4/en/manual/api/reference/hostinterface/object"""
from zabbix_enums import _ZabbixEnum

class HostInterfaceAvailable(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.4/en/manual/api/reference/hostinterface/object#host-interface

    [Readonly]
    Availability of host interface.
    """
    UNKNOWN = 0
    AVAILABLE = 1
    UNAVAILABLE = 2


class HostInterfaceMain(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.4/en/manual/api/reference/hostinterface/object#host-interface

    Whether the interface is used as default on the host.
    Only one interface of some type can be set as default on a host.
    """
    NO = 0
    YES = 1


class HostInterfaceType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.4/en/manual/api/reference/hostinterface/object#host-interface

    Interface type.
    """
    AGENT = 1
    SNMP = 2
    IPMI = 3
    JMX = 4


class HostInterfaceUseIP(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.4/en/manual/api/reference/hostinterface/object#host-interface

    Whether the connection should be made via IP.
    """
    NO = 0
    YES = 1


class DetailsTagVersion(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.4/en/manual/api/reference/hostinterface/object#details-tag

    SNMP interface version.
    """
    SNMP1 = 1
    SNMP2 = 2
    SNMP3 = 3


class DetailsTagBulk(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.4/en/manual/api/reference/hostinterface/object#details-tag

    Whether to use bulk SNMP requests.
    """
    NO = 0
    YES = 1


class DetailsTagSecurityLevel(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.4/en/manual/api/reference/hostinterface/object#details-tag

    SNMPv3 security level.
    Used only by SNMPv3 interfaces.
    """
    NOAUTHNOPRIV = 0
    AUTHNOPRIV = 1
    AUTHPRIV = 2


class DetailsTagAuthProtocol(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.4/en/manual/api/reference/hostinterface/object#details-tag

    SNMPv3 authentication protocol.
    Used only by SNMPv3 interfaces.
    """
    MD5 = 0
    SHA = 1


class DetailsTagPrivProtocol(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.4/en/manual/api/reference/hostinterface/object#details-tag

    SNMPv3 privacy protocol.
    Used only by SNMPv3 interfaces.
    """
    DES = 0
    AES = 1
