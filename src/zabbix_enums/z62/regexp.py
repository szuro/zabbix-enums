"""https://www.zabbix.com/documentation/current/en/manual/api/reference/regexp/object"""
from zabbix_enums import _ZabbixEnum


class ExpressionObjectExpressionType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/current/en/manual/api/reference/regexp/object#expressions-object

    Type of Regular expression.
    """
    STRING_INCLUDED = 0
    ANY_STRING_INCLUDED = 1
    STRING_NOT_INCLUDED = 2
    RESULT_IS_TRUE = 3
    RESULT_IS_FALSE = 4


class ExpressionObjectCaseSensitive(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/current/en/manual/api/reference/regexp/object#expressions-object

    Case sensitivity.
    """
    OFF = 0
    ON = 1
    NO = 0
    YES = 1
