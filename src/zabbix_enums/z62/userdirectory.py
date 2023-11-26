"""https://www.zabbix.com/documentation/6.2/en/manual/api/reference/userdirectory/object"""
from zabbix_enums import _ZabbixEnum


class UserDirectoryStartTLS(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.2/en/manual/api/reference/userdirectory/object
    
    LDAP startTLS option. It cannot be used with ldaps:// protocol hosts.
    """
    disabled = 0
    enabled = 1
