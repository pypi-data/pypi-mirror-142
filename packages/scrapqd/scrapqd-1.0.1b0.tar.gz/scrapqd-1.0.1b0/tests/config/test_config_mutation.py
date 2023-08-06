import unittest

from scrapqd.settings import config


class TestConfigMutation(unittest.TestCase):
    def test_config_clear(self):
        with self.assertRaises(AttributeError):
            config.USER_AGENTS.clear()

    def test_config_assign(self):
        with self.assertRaises(TypeError):
            config.USER_AGENTS[0] = None
