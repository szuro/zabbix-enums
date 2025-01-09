"""https://www.zabbix.com/documentation/7.2/en/manual/api/reference/image/object"""
from zabbix_enums import _ZabbixEnum


class ImageType(_ZabbixEnum):
    """
    https://www.zabbix.com/documentation/7.2/en/manual/api/reference/image/object#image
    
    Type of image.
    """
    ICON = 1
    BACKGROUND_IMAGE = 2
