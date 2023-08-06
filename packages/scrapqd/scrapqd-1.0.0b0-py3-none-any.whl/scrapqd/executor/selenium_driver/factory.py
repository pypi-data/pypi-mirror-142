from scrapqd.executor.exception import BrowserNotSupportedConfigError
from scrapqd.executor.selenium_driver.browsers import Firefox, GoogleChrome
from scrapqd.factory_interface import ConfigItem
from scrapqd.settings import config


class BrowserFactory(ConfigItem):
    """Combines system browser mapping and user config"""

    def __init__(self):
        super().__init__(config=config.BROWSERS,
                         exception=BrowserNotSupportedConfigError,
                         default_config={
                             "FIREFOX": Firefox,
                             "GOOGLE_CHROME": GoogleChrome,
                         },
                         default_item=config.DEFAULT_BROWSER)
