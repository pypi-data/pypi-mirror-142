import logging

from selenium.webdriver import Chrome
from selenium.webdriver import Firefox as FirefoxDriver
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.chrome.options import Options as COptions
from selenium.webdriver.firefox.options import Options as FFOptions
from webdriver_manager.utils import ChromeType

from scrapqd.executor.selenium_driver.selenium import SeleniumDriver
from scrapqd.settings import config

logger = logging.getLogger(__name__)


class GoogleChrome(SeleniumDriver):
    """Creates Google Chrome type driver"""

    @classmethod
    def create_browser(cls):
        """Returns headless Google browser object"""

        chrome_options = COptions()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        version = config.CHROMIUM_VERSION if hasattr(config,
                                                     "CHROMIUM_VERSION") and config.CHROMIUM_VERSION else "latest"
        browser = Chrome(options=chrome_options,
                         executable_path=cls.get_executable_path(browser=ChromeType.GOOGLE,
                                                                 version=version))
        return browser


class Firefox(SeleniumDriver):
    """Creates Firefox type driver"""

    @classmethod
    def create_browser(cls):
        """Returns headless Firefox object"""

        FirefoxProfile().set_preference("intl.accept_languages", "es")
        opts = FFOptions()
        opts.headless = True
        version = config.GECKODRIVER_VERSION if hasattr(config,
                                                        "GECKODRIVER_VERSION") and config.GECKODRIVER_VERSION else "latest"
        browser = FirefoxDriver(options=opts,
                                executable_path=cls.get_executable_path(browser="FIREFOX",
                                                                        version=version))
        return browser
