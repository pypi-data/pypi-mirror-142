from scrapqd.executor.requests import Requests
from scrapqd.executor.selenium import Selenium
from scrapqd.factory_interface import ConfigItem
from scrapqd.fetch.exception import CrawlerNotSupportedError
from scrapqd.settings import config


class ExecutorFactory(ConfigItem):
    """Combines system executor mapping and user config"""

    def __init__(self):
        super().__init__(config=config.CRAWLERS,
                         exception=CrawlerNotSupportedError,
                         default_config={
                             "REQUESTS": Requests,
                             "SELENIUM": Selenium,
                         },
                         default_item="REQUESTS")
