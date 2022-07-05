"""https://www.zabbix.com/documentation/5.0/en/manual/api/reference/httptest/object"""
from zabbix_enums import _ZabbixEnum


class WebScenarioAuthentication(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/httptest/object#web-scenario
    
    Authentication method that will be used by the web scenario.
    """
    NONE = 0
    BASIC = 1
    NTLM = 2

class WebScenarioStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/httptest/object#web-scenario
    
    Whether the web scenario is enabled.
    """
    ENABLED = 0
    DISABLED = 1


class WebScenarioVerifyHost(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/httptest/object#web-scenario
    
    Whether to verify that the host name specified in the SSL certificate matches the one used in the scenario.
    """
    NO = 0
    YES = 1


class WebScenarioVerifyPeer(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/httptest/object#web-scenario

    Whether to verify the SSL certificate of the web server.
    """
    NO = 0
    YES = 1



class ScenarioStepFollowredirects(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/httptest/object#scenario-step
    
    Whether to follow HTTP redirects.
    """
    NO = 0
    YES = 1

class ScenarioStepRetrieveMode(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.0/en/manual/api/reference/httptest/object#scenario-step
    
    Part of the HTTP response that the scenario step must retrieve.
    """
    BODY = 0
    HEADERS = 1
    BODY_AND_HEADERS = 2
    BOTH = 2
