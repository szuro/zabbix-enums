from copy import deepcopy
from types import ModuleType


def _apply_mapping(entity, mapping):
    for field, enumeration in mapping.items():
        if enumeration is None:
            continue
        if field in entity:
            entity[field] = enumeration(entity[field])


def _enumify_members(obj, enum_library, mapping: dict):
    for member, funct in mapping.items():
        if member in obj and funct is not None:
            obj[member] = [funct(x, enum_library) for x in obj[member]]


def _enumify_entity(obj, field_mapping, members, enum_library: ModuleType, deep_enumify: bool = False):
    obj = deepcopy(obj)
    _apply_mapping(obj, field_mapping)
    if deep_enumify:
        _enumify_members(obj, enum_library, members)
    return obj


def enumify_host(host: dict, enum_library: ModuleType, deep_enumify: bool = False):
    field_mapping = {
        'available': None,
        'flags': enum_library.HostFlag,
        'inventory_mode': enum_library.HostInventoryMode,
        'ipmi_authtype': None,
        'ipmi_available': None,
        'ipmi_privilege': None,
        'jmx_available': None,
        'maintenance_status': enum_library.HostMaintenanceStatus,
        'maintenance_type': None,
        'snmp_available': None,
        'status': enum_library.HostStatus,
        'tls_connect': None,
        'tls_accept': None
    }
    members = {
        'items': enumify_item,
        'triggers': enumify_trigger,
        'interfaces': enumify_interface
    }
    host = _enumify_entity(host, field_mapping, members, enum_library, deep_enumify)
    return host


def enumify_item(item: dict, enum_library: ModuleType, deep_enumify: bool = False) -> dict:
    field_mapping = {
        'type': enum_library.ItemType,
        'value_type': enum_library.ItemValueType,
        'allow_traps': enum_library.ItemAllowTraps,
        'flags': enum_library.ItemFlag,
        'follow_redirects': enum_library.ItemFollowRedirects,
        'inventory_link': enum_library.HostInventoryProperty,
        'output_format': enum_library.ItemOutputFormat,
        'post_type': enum_library.ItemPostType,
        'request_method': enum_library.ItemRetrieveMode,
        'retrieve_mode': enum_library.ItemRetrieveMode,
        'state': enum_library.ItemState,
        'status': enum_library.ItemStatus,
        'verify_host': enum_library.ItemVerifyHost,
        'verify_peer': enum_library.ItemVerifyPeer,
    }
    members = {}
    item = _enumify_entity(item, field_mapping, members, enum_library, deep_enumify)

    if 'authtype' in item:
        if 'type' in item and item['type'] is enum_library.ItemType.HTTP:
            item['authtype'] = enum_library.ItemAuthTypeHTTP(item['authtype'])
        else:
            item['authtype'] = enum_library.ItemAuthTypeSSH(item['authtype'])

    return item


def enumify_trigger(trigger: dict, enum_library: ModuleType, deep_enumify: bool = False) -> dict:
    field_mapping = {
        'flags': enum_library.TriggerFlag,
        'priority': enum_library.TriggerPriority,
        'state': enum_library.TriggerState,
        'status': enum_library.TriggerStatus,
        'type': enum_library.TriggerType,
        'value': enum_library.TriggerValue,
        'recovery_mode': enum_library.TriggerRecoveryMode,
        'correlation_mode': enum_library.TriggerCorrelationMode,
        'manual_close': enum_library.TriggerManualClose
    }
    members = {
        'groups': None,
        'hosts': enumify_host,
        'items': enumify_item,
        'lastEvent': None,
        'discoveryRule': None
    }
    trigger = _enumify_entity(trigger, field_mapping, members, enum_library, deep_enumify)
    return trigger


def enumify_interface(interface: dict, enum_library: ModuleType, deep_enumify: bool = False) -> dict:
    field_mapping = {
        'main': enum_library.HostInterfaceMain,
        'type': enum_library.HostInterfaceType,
        'useip': enum_library.HostIntrefaceUseIP
    }
    members = {
        'items': enumify_item,
        'hosts': enumify_host
    }
    interface = _enumify_entity(interface, field_mapping, members, enum_library, deep_enumify)
    return interface
