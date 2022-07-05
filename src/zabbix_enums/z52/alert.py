"""https://www.zabbix.com/documentation/5.2/en/manual/api/reference/alert/object"""
from zabbix_enums import _ZabbixEnum


class AlertType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/alert/object#alert
    
    Alert type.
    """
    MESSAGE = 0
    REMOTE_COMMAND = 1


class AlertStatusMessage(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/alert/object#alert
    
    Status indicating whether the action operation has been executed successfully.
    Possible values for message alerts.
    """
    MESSAGE_NOT_SENT = 0
    MESSAGE_SENT = 1
    FAILED_AFTER_RETRIES = 2
    NOT_YET_PROCESSE = 3


class AlertStatusCommand(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/5.2/en/manual/api/reference/alert/object#alert
    
    Status indicating whether the action operation has been executed successfully.
    Possible values for command alerts.
    """
    COMMAND_NOT_RUN = 0
    COMMAND_RUN = 1
    TRIED_TO_RUN = 2
