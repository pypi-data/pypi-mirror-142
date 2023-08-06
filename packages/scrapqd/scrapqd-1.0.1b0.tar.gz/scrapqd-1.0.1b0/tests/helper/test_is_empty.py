import unittest

from scrapqd.common.helper import is_empty


class TestUserConfig(unittest.TestCase):

    def test_is_empty_str(self):
        xpath = ""
        self.assertTrue(is_empty(xpath))

    def test_is_empty_set(self):
        values = set()
        self.assertTrue(is_empty(values))

    def test_is_empty_frozenset(self):
        values = frozenset()
        self.assertTrue(is_empty(values))

    def test_is_empty_dict(self):
        values = {}
        self.assertTrue(is_empty(values))

    def test_is_empty_dict_values(self):
        values = {"user": "Durai"}
        self.assertFalse(is_empty(values))

    def test_is_empty_non_present_mapping(self):
        from types import MappingProxyType
        values = MappingProxyType({})
        self.assertFalse(is_empty(values))
