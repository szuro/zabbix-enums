"""https://www.zabbix.com/documentation/7.0/en/manual/api/reference/connector/object"""
from zabbix_enums import _ZabbixEnum

class ConnectorProtocol(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/connector/object#connector

    Communication protocol.
    """
    ZABBIX_STREAMING_PROTOCOL_V1 = 0


class ConnectorDataType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/connector/object#connector

    Data type.
    """
    ITEM_VALUES = 0
    EVENTS = 1


class ConnectorItemValueType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/connector/object#connector

    A sum of item value types to be sent.
    """
    NUMERIC_FLOAT = 1
    FLOAT = 1
    CHARACTER = 2
    LOG = 4
    NUMERIC_UNSIGNED = 8
    UNSIGNED = 8
    TEXT = 10
    BINARY = 20
    ALL = 31


class ConnectorAuthType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/connector/object#connector

    HTTP authentication method.
    """
    NONE = 0
    BASIC = 1
    NTLM = 2
    KERBEROS = 3
    DIGEST = 4
    BEARER = 5

class ConnectorVerifyPeer(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/connector/object#connector
    
    Whether to validate that the host's certificate is authentic.
    """
    NO = 0
    YES = 1

class ConnectorVerifyHost(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/connector/object#connector
    
    Whether to validate that the host name for the connection matches the one in the host's certificate.
    """
    NO = 0
    YES = 1


class ConnectorStatus(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/connector/object#connector
    
    Whether the connector is enabled.
    """
    DISABLED = 0
    ENABLED = 1


class ConnectorTagsEvaltType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/connector/object#connector
    
    Tag evaluation method.
    """
    AND_OR = 0
    OR = 2


class TagFilerOperator(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.0/en/manual/api/reference/connector/object#tag-filter
    
    Condition operator.
    """
    EQUALS = 0
    DOES_NOT_EQUAL = 1
    CONTAINS = 2
    DOES_NOT_CONTAIN = 3
    EXISTS = 12
    DOES_NOT_EXIST = 1 #TODO
