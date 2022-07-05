"""https://www.zabbix.com/documentation/5.2/en/manual/api/reference/authentication/object"""
from zabbix_enums import _ZabbixEnum


class AuthenticationType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/authentication/object#authentication

    Default authentication.
    """
    INTERNAL = 0
    LDAP = 1


class AuthenticationHTTPAuthEnabled(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/authentication/object#authentication

    Enable HTTP authentication.
    """
    DISABLED = 0
    ENABLED = 1


class AuthenticationHTTPLoginForm(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/authentication/object#authentication

    Default login form.
    """
    ZABBIX_FORM = 0
    HTTP_FORM = 1


class AuthenticationHTTPCaseSensitive(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/authentication/object#authentication

    HTTP case sensitive login.
    """
    OFF = 0
    ON = 1
    NO = 0
    YES = 1


class AuthenticationLDAPConfigured(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/authentication/object#authentication

    Enable LDAP authentication
    """
    DISABLED = 0
    ENABLED = 1


class AuthenticationLDAPCaseSensitive(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/authentication/object#authentication

    LDAP case sensitive login.
    """
    OFF = 0
    ON = 1
    NO = 0
    YES = 1


class AuthenticationSAMLAuthEnabled(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/authentication/object#authentication

    Enable SAML authentication
    """
    DISABLED = 0
    ENABLED = 1


class AuthenticationSAMLSignMessages(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/authentication/object#authentication

    SAML sign messages.
    """
    NO = 0
    YES = 1


class AuthenticationSAMLSignAssertions(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/authentication/object#authentication

    SAML sign assertions.
    """
    NO = 0
    YES = 1


class AuthenticationSAMLSignAuthnrequests(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/authentication/object#authentication

    SAML sign AuthN requests.
    """
    NO = 0
    YES = 1


class AuthenticationSAMLSignLogoutRequests(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/authentication/object#authentication

    SAML sign logout requests.
    """
    NO = 0
    YES = 1


class AuthenticationSAMLSignLogoutResponses(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/authentication/object#authentication

    SAML sign logout responses.
    """
    NO = 0
    YES = 1


class AuthenticationSAMLEncryptNameId(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/authentication/object#authentication

    SAML encrypt name ID.
    """
    NO = 0
    YES = 1


class AuthenticationSAMLEncryptAssertions(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/authentication/object#authentication

    SAML encrypt assertions.
    """
    NO = 0
    YES = 1


class AuthenticationSAMLCaseSensitive(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/authentication/object#authentication

    SAML case sensitive login.
    """
    OFF = 0
    ON = 1
    NO = 0
    YES = 1
