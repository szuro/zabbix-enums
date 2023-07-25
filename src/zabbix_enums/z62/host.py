"""https://www.zabbix.com/documentation/6.2/en/manual/api/reference/host/object"""
from zabbix_enums import _ZabbixEnum


class HostFlag(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/host/object#host

    [Readonly]
    Origin of the host.
    """
    PLAIN = 0
    DISCOVERED = 4


class HostInventoryMode(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/host/object#host

    Host inventory population mode.
    """
    DISABLED = -1
    MANUAL = 0
    AUTOMATIC = 1


class HostIPMIAuthType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/host/object#host

    IPMI authentication algorithm.
    """
    DEFAULT = -1
    NONE = 0
    MD2 = 1
    MD = 2
    STRAIGHT = 4
    OEM = 5
    RMCP = 6


class HostIPMIPrivilege(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/host/object#host

    IPMI privilege level.
    """
    CALLBACK = 1
    USER = 2
    OPERATOR = 3
    ADMIN = 4
    OEM = 5


class HostMaintenanceStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/host/object#host

    [Readonly]
    Effective maintenance type.
    """
    NO_MAINTENANCE = 0
    IN_MAINTENANCE = 1


class HostMaintenanceType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/host/object#host

    [Readonly]
    Effective maintenance type.
    """
    WITH_DATA_COLLECTION = 0
    WITHOUT_DATA_COLLECTION = 1


class HostStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/host/object#host

    Status and function of the host.
    """
    MONITORED = 0
    UNMONITORED = 1


class HostTLSConnect(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/host/object#host

    Connections to host.
    """
    NO_ENCRYPTION = 1
    PSK = 2
    CERTIFICATE = 4


class HostTLSAccept(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/host/object#host

    Connections from host.
    Possible bitmap values.
    """
    NO_ENCRYPTION = 1
    PSK = 2
    CERTIFICATE = 4


class HostActiveAvailable(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/host/object#host

    [Readonly]
    Host active interface availability status
    """
    UNKNOWN = 0
    AVAILABLE = 1
    UNAVAILABLE = 2


class HostInventoryProperty(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/host/object#host-inventory

    Each property has it's own unique ID number,
    which is used to associate host inventory fields with items. 
    """
    ALIAS = 4
    ASSET_TAG = 11
    CHASSIS = 28
    CONTACT = 23
    CONTRACT_NUMBER = 32
    DATE_HW_DECOMM = 47
    DATE_HW_EXPIRY = 46
    DATE_HW_INSTALL = 45
    DATE_HW_PURCHASE = 44
    DEPLOYMENT_STATUS = 34
    HARDWARE = 14
    HARDWARE_FULL = 15
    HOST_NETMASK = 39
    HOST_NETWORKS = 38
    HOST_ROUTER = 40
    HW_ARCH = 30
    INSTALLER_NAME = 33
    LOCATION = 24
    LOCATION_LAT = 25
    LOCATION_LON = 26
    MACADDRESS_A = 12
    MACADDRESS_B = 13
    MODEL = 29
    NAME = 3
    NOTES = 27
    OOB_IP = 41
    OOB_NETMASK = 42
    OOB_ROUTER = 43
    OS = 5
    OS_FULL = 6
    OS_SHORT = 7
    POC_1_CELL = 61
    POC_1_EMAIL = 58
    POC_1_NAME = 57
    POC_1_NOTES = 63
    POC_1_PHONE_A = 59
    POC_1_PHONE_B = 60
    POC_1_SCREEN = 62
    POC_2_CELL = 68
    POC_2_EMAIL = 65
    POC_2_NAME = 64
    POC_2_NOTES = 70
    POC_2_PHONE_A = 66
    POC_2_PHONE_B = 67
    POC_2_SCREEN = 69
    SERIALNO_A = 8
    SERIALNO_B = 9
    SITE_ADDRESS_A = 48
    SITE_ADDRESS_B = 49
    SITE_ADDRESS_C = 50
    SITE_CITY = 51
    SITE_COUNTRY = 53
    SITE_NOTES = 56
    SITE_RACK = 55
    SITE_STATE = 52
    SITE_ZIP = 54
    SOFTWARE = 16
    SOFTWARE_APP_A = 18
    SOFTWARE_APP_B = 19
    SOFTWARE_APP_C = 20
    SOFTWARE_APP_D = 21
    SOFTWARE_APP_E = 22
    SOFTWARE_FULL = 17
    TAG = 10
    TYPE = 1
    TYPE_FULL = 2
    URL_A = 35
    URL_B = 36
    URL_C = 37
    VENDOR = 31


class HostHostTagAutomatic(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/host/object#host-tag

    Type of host tag.
    """
    MANUAL = 0
    AUTOMATIC = 1
