from unittest import TestCase
from zabbix_enums.common import _ZabbixEnum


class TestEnum(_ZabbixEnum):
    VAL = 0


class TestZEnum(TestCase):
    def test_str(self):
        self.assertTrue(TestEnum('0') is TestEnum.VAL)

    def test_int(self):
        self.assertTrue(TestEnum(0) is TestEnum.VAL)

    def test_notfound_str(self):
        with self.assertRaisesRegex(ValueError, '1 is not a valid TestEnum'):
            TestEnum('1')

    def test_notfound_int(self):
        with self.assertRaisesRegex(ValueError, '1 is not a valid TestEnum'):
            TestEnum(1)

    def test_invalid_str(self):
        with self.assertRaisesRegex(ValueError, "invalid literal for int\(\) with base 10: 'kotek'"):
            TestEnum('kotek')
