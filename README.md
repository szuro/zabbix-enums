# zabbix-enums

Zabbix enumerations for API scripting.


This package aims to provide enumerations for Zabbix object parameters.
So instead of using bare numbers and constantly browsing the docs, you can just use a nice enum.

Take the following code as an example:

```python
from zabbix_enums.z54 import TriggerState
from pyzabbix import ZabbixAPI

zapi = ZabbixAPI('http://localhost')
zapi.login('Admin', 'zabbix')

# this
unknown_triggers = zapi.trigger.get(filter={'state': 1})
# becomes this
unknown_triggers = zapi.trigger.get(filter={'state': TriggerState.UNKNOWN})

```

Another use case is checking entity state:

```python

from zabbix_enums.z54 import HostStatus
from pyzabbix import ZabbixAPI


zapi = ZabbixAPI('http://localhost')
zapi.login('Admin', 'zabbix')

hosts = zapi.host.get()

monitored = [host for host in hosts if HostStatus(host['status']) is HostStatus.MONITORED]

```

# Limitations
Please bare in mind that not all enumerations are present at this time.
