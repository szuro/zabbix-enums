
from unittest import TestCase
import warnings
import os
import importlib


class TestImports(TestCase):
    def test_latest_imports(self):
        from zabbix_enums.latest.host import HostStatus as LatestHostStatus
        from zabbix_enums.z74.host import HostStatus as Z74HostStatus
        self.assertTrue(LatestHostStatus is Z74HostStatus, "LatestHostStatus should be the same as Z74HostStatus")
    
    def test_latest_lts_imports(self):
        from zabbix_enums.latest_lts.host import HostStatus as LatestLTSHostStatus
        from zabbix_enums.z70.host import HostStatus as Z70HostStatus
        self.assertTrue(LatestLTSHostStatus is Z70HostStatus, "LatestLTSHostStatus should be the same as Z70HostStatus")