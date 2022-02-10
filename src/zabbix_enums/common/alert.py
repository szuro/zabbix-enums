from zabbix_enums.common import _ZabbixEnum


class AlertType(_ZabbixEnum):
    MESSAGE = 0
    REMOTE_COMMAND = 1

class MessageAlert(_ZabbixEnum):
    MESSAGE_NOT_SENT = 0
    MESSAGE_SENT = 1
    FAILED_AFTER_RETRIES = 2
    NOT_YET_PROCESSE = 3

class CommandAlert(_ZabbixEnum):
    COMMAND_NOT_RUN = 0
    COMMAND_RUN = 1
    TRIED_TO_RUN = 2
