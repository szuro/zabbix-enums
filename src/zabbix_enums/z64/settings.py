"""https://www.zabbix.com/documentation/6.4/en/manual/api/reference/settings/object"""
from zabbix_enums import _ZabbixEnum


class SettingsServerCheckInterval(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.4/en/manual/api/reference/settings/object#settings

    Show warning if Zabbix server is down.
    """
    DONT_SHOW_WARNING = 0
    SHOW_WARNING = 10


class SettingsShowTechnicalErrors(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.4/en/manual/api/reference/settings/object#settings

    Show technical errors (PHP/SQL) to non-Super admin users and to users that are not part of user groups with debug mode enabled.
    """
    NO = 0
    YES = 1


class SettingsCustomColor(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.4/en/manual/api/reference/settings/object#settings

    Use custom event status colors.
    """
    NO = 0
    YES = 1


class SettingsProblemUnackStyle(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.4/en/manual/api/reference/settings/object#settings

    Blinking for unacknowledged PROBLEM events.
    """
    DONT_BLINK = 0
    BLINK = 1


class SettingsProblemAckStyle(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.4/en/manual/api/reference/settings/object#settings

    Blinking for acknowledged PROBLEM events.
    """
    DONT_BLINK = 0
    BLINK = 1


class SettingsOKUnackStyle(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.4/en/manual/api/reference/settings/object#settings

    Blinking for unacknowledged RESOLVED events.
    """
    DONT_BLINK = 0
    BLINK = 1


class SettingsOKAckStyle(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.4/en/manual/api/reference/settings/object#settings

    Blinking for acknowledged RESOLVED events.
    """
    DONT_BLINK = 0
    BLINK = 1


class SettingsDefaultInventoryMode(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.4/en/manual/api/reference/settings/object#settings

    Default host inventory mode.
    """
    DISABLED = -1
    MANUAL = 0
    AUTOMATIC = 1


class SettingsSnmptrapLogging(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.4/en/manual/api/reference/settings/object#settings

    Log unmatched SNMP traps.
    """
    NO = 0
    YES = 1


class SettingsValidateUriSchemes(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.4/en/manual/api/reference/settings/object#settings

    Validate URI schemes.
    """
    NO = 0
    YES = 1


class SettingsIframeSandboxingEnabled(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.4/en/manual/api/reference/settings/object#settings

    Use iframe sandboxing.
    """
    NO = 0
    YES = 1

class SettingsAuditlogEnabled(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.4/en/manual/api/reference/settings/object#settings

    Enable audit logging.
    """
    NO = 0
    YES = 1

class SettingsVaultProvider(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/6.4/en/manual/api/reference/settings/object#settings

    Vault provider.
    """
    HASHICORP = 0
    CYBERARK = 1
