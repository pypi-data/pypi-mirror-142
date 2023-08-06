from abc import ABC

from scrapqd.common.helper import is_empty


class ConfigItem(ABC):
    """This is an interface class for configuration item which needs to be combined with system default config."""

    def __init__(self, config, exception, default_config, default_item, upper_keys=True):
        """
        This class is for internal use to combine configurations such as CRAWLERS, BROWSERS, FIELDS.

        :param config: user configuration
        :param exception: exceptions to be raised when the user configuration clashes system default configuration
        :param default_config: system default configuration.
        :param default_item: default to be used in the system after combining the configuration
                Example: in BROWSERS configuration, GOOGLE_CHROME is default.
        :param upper_keys: keys to be in uppercase or not
        """
        self.exception = exception
        self.config = config
        self.default_config = default_config
        self.default_item = default_item
        self.upper_keys = upper_keys

    def get_key(self, name):
        """Gets the upper case key if upper_keys flag is set otherwise return the same key"""
        if self.upper_keys:
            return name.upper()
        return name

    def mapping(self):
        """Combines the user and system configuration"""
        user_items = self.config
        items_mapping = self.default_config
        for item in self.config:
            item = self.get_key(item)
            if item in items_mapping:
                raise self.exception(item)
            items_mapping[item] = user_items[item]

        return items_mapping

    def get(self, name=None):
        """Gets the appropriate config value from the mapping"""
        if is_empty(name) and self.default_item is not None:
            name = self.default_item

        name = self.get_key(name)
        mapping = self.mapping()
        return mapping[name]
