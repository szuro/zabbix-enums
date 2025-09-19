"""https://www.zabbix.com/documentation/7.4/en/manual/api/reference/userdirectory/object"""
from zabbix_enums import _ZabbixEnum


class UserDirectoryIdpType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/userdirectory/object

    Type of the authentication protocol used by the identity provider for the user directory.
    """
    LDAP = 1
    SAML = 2


class UserDirectoryProvisionStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/userdirectory/object

    Provisioning status of the user directory.
    """
    DISABLED = 0
    ENABLED = 1


class UserDirectoryLDAPStartTLS(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/userdirectory/object

    LDAP startTLS option. It cannot be used with ldaps:// protocol hosts.
    """
    DISABLED = 0
    ENABLED = 1


class UserDirectorySAMLEncryptNameId(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/userdirectory/object#user-directory

    SAML encrypt name ID.
    """
    NO = 0
    YES = 1


class UserDirectorySAMLEncryptAssertions(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/userdirectory/object#user-directory

    SAML encrypt assertions.
    """
    NO = 0
    YES = 1


class UserDirectorySCIMStatus(_ZabbixEnum):
    """

 	Whether SCIM provisioning for SAML is enabled or disabled.
    """
    DISABLED = 0
    ENABLED = 1


class UserDirectorySAMLSignAssertions(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/userdirectory/object#user-directory

    SAML sign assertions.
    """
    NO = 0
    YES = 1


class UserDirectorySAMLSignAuthnRequests(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/userdirectory/object#user-directory

    SAML sign AuthN requests.
    """
    NO = 0
    YES = 1


class UserDirectorySAMLSignMessages(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/userdirectory/object#user-directory

    SAML sign messages.
    """
    NO = 0
    YES = 1


class UserDirectorySAMLSignLogoutRequests(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/userdirectory/object#user-directory

    SAML sign logout requests.
    """
    NO = 0
    YES = 1


class UserDirectorySAMLSignLogoutResponses(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/userdirectory/object#user-directory

    SAML sign logout responses.
    """
    NO = 0
    YES = 1


class UserDirectoryMediaTypeMappingsActive(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/userdirectory/object#media-type-mappings

    User media active property value when media is created for the provisioned user.
    """
    ENABLED = 0
    DISABLED = 1
