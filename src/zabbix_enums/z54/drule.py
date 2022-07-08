"""https://www.zabbix.com/documentation/5.4/en/manual/api/reference/drule/object"""
from zabbix_enums import _ZabbixEnum


class DiscoveryRuleStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.4/en/manual/api/reference/drule/object#discovery-rule

    Whether the discovery rule is enabled.
    """
    ENABLED = 0
    DISABLED = 1
