"""https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostprototype/object"""
from zabbix_enums import _ZabbixEnum


class HostPrototypeStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostprototype/object#host-prototype

    Status of the host prototype.
    """
    MONITORED = 0
    UNMONITORED = 1


class HostPrototypeInventoryMode(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostprototype/object#host-prototype

    Host inventory population mode.
    """
    DISABLED = -1
    MANUAL = 0
    AUTOMATIC = 1


class HostPrototypeDiscover(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostprototype/object#host-prototype

    Host prototype discovery status.
    """
    DISCOVER = 0
    DONT_DISCOVER = 1


class HostPrototypeCustomInterfaces(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostprototype/object#host-prototype

    Source of interfaces for hosts created by the host prototype.
    """
    PARENT_HOST = 0
    CUSTOM_INTERFACE = 1


class CustomInterfaceMain(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostprototype/object#custom-interface

    Whether the interface is used as default on the host.
    Only one interface of some type can be set as default on a host.
    """


class CustomInterfaceType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostprototype/object#custom-interface

    Interface type.
    """
    AGENT = 1
    SNMP = 2
    IPMI = 3
    JMX = 4


class CustomInterfaceUseIp(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostprototype/object#custom-interface

    Whether the connection should be made via IP.
    """
    NO = 0
    YES = 1


class CustomInterfaceDetailsVersion(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostprototype/object#custom-interface-details

    SNMP interface version.
    """
    SNMP1 = 1
    SNMP2 = 2
    SNMP3 = 3


class CustomInterfaceDetailsBulk(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostprototype/object#custom-interface-details

    Whether to use bulk SNMP requests.
    """
    NO = 0
    YES = 1


class CustomInterfaceDetailsSecurityLevel(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostprototype/object#custom-interface-details

    SNMPv3 security level.
    Used only by SNMPv3 interfaces.
    """
    NOAUTHNOPRIV = 0
    AUTHNOPRIV = 1
    AUTHPRIV = 2


class CustomInterfaceDetailsAuthProtocol(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostprototype/object#custom-interface-details

    SNMPv3 authentication protocol.
    Used only by SNMPv3 interfaces.
    """
    MD5 = 0
    SHA = 1
    SHA1 = 1
    SHA224 = 2
    SHA256 = 3
    SHA384 = 4
    SHA512 = 5


class CustomInterfaceDetailsPrivProtocol(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/hostprototype/object#custom-interface-details

    SNMPv3 privacy protocol.
    Used only by SNMPv3 interfaces.
    """
    DES = 0
    AES = 1
    AES128 = 1
    AES192 = 2
    AES256 = 3
    AES192C = 4
    AES256C = 5
