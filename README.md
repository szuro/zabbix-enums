# zabbix-enums

Zabbix enumerations for API scripting.


This package aims to provide enumerations for Zabbix object parameters.
So instead of using bare numbers and constantly browsing the docs, you can just use a nice enum.

Example 1:
Use nice enums in API calls

```python
from zabbix_enums.z60 import TriggerState
from pyzabbix import ZabbixAPI

zapi = ZabbixAPI('http://localhost')
zapi.login('Admin', 'zabbix')

# this
unknown_triggers = zapi.trigger.get(filter={'state': 1})
# becomes this
unknown_triggers = zapi.trigger.get(filter={'state': TriggerState.UNKNOWN})


zapi.user.logout()
```

Example 2:
Filter entities offline, based on their status

```python
from zabbix_enums.z60 import HostStatus
from pyzabbix import ZabbixAPI


zapi = ZabbixAPI('http://localhost')
zapi.login('Admin', 'zabbix')

hosts = zapi.host.get()

monitored = [h for h in hosts if HostStatus(h['status']) == HostStatus.MONITORED]

zapi.user.logout()

```

Example 3:
Filter problems with severities above a certain level

```python
from zabbix_enums.z60 import ProblemSeverity
from pyzabbix import ZabbixAPI


zapi = ZabbixAPI('http://localhost')
zapi.login('Admin', 'zabbix')

problems = zapi.problem.get()

important = [p for p in problems if ProblemSeverity(p['severity']) > ProblemSeverity.AVERAGE]

zapi.user.logout()
```

# Limitations
Please bare in mind that not all enumerations are present at this time.
For comparing Enums do not use `is` keyword - see second example

At this moment, only Zabbix 5.0 and above is supported.

# Versioning
The following version schema is used: X.Y.Z

X - major version. If this changes, your code might break - update with caution.

Y - latest supported Zabbix version. I.E 1.60.0 supports Zabbix 6.0 and below but not 6.2.

Z - minor version. For bugfixes.
