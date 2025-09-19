"""https://www.zabbix.com/documentation/7.4/en/manual/api/reference/template/object"""
from zabbix_enums import _ZabbixEnum


class TemplateWizardReady(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.4/en/manual/api/reference/template/object

    Whether the template is available for selection in the Host Wizard.
    """
    NO = 0
    YES = 1
