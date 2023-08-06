import re
from abc import ABC, abstractmethod

from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.utils import ChromeType

from scrapqd.common.helper import is_empty
from scrapqd.executor.exception import BrowserNotSupportedError


class DocumentReady:
    """Custom class for checking state of the request in selenium executor."""

    def __init__(self, xpath=None):
        """Creates DocumentReady instance

        :param xpath: path to locate element
        """
        self.xpath = xpath

    def __call__(self, browser):
        if self.xpath:
            element = browser.find_element_by_xpath(self.xpath)
            document_ready = bool(element)
        else:
            # if the xpath is not provided, javascript is executed in browser
            # to check state of the document
            document_state = browser.execute_script("return document.readyState")
            document_ready = document_state == "complete"

        return document_ready


class SeleniumDriver(ABC):
    """Internal selenium driver implementation for all the browser types"""

    def __init__(self):
        """Creates SeleniumDriver instance and creates requested browser pool."""

        self.browser = self.create_browser()
        self.response_headers = None
        self.DEFAULT_WAIT_TIME = 30  # in seconds

    @classmethod
    @abstractmethod
    def create_browser(cls):
        pass

    def wait_load(self, xpath, wait_time):
        """Waits for browser to load specific element in the given url. If the xpath is not given,
        selenium will wait for the document to be ready.

        :param xpath: element to wait
        :param wait_time: wait time in seconds for the element to present in the web page.
        """
        wait = WebDriverWait(self.browser, wait_time)
        wait.until(DocumentReady(xpath=xpath))

    def fetch(self, url, **kwargs):
        """Fetches web page for the url

        :param url: url to crawl
        :param kwargs:
                    - wait - wait time in seconds for the element in the web page.
                    - xpath - element to wait. If this parameter is not given, selenium will wait for the document
                                to be ready till wait time.
        """

        options = kwargs.get("options", self.DEFAULT_WAIT_TIME)
        wait_time = options.get("wait_time", self.DEFAULT_WAIT_TIME)
        xpath = kwargs.get("xpath", None)
        if is_empty(xpath):
            xpath = None
        self.browser.get(url)
        self.wait_load(xpath=xpath, wait_time=wait_time)

    def get_response_headers(self):
        """This executes javascript in the browser to get http response headers.

        :return: Dict
        """
        response_headers = self.browser.execute_script("""
                       var req = new XMLHttpRequest();
                       req.open("GET", document.location, false);
                       req.send(null);
                       return req.getAllResponseHeaders()
               """)
        response_headers = re.findall("(?P<key>.*):(?P<value>.*)\r\n", response_headers)
        response_headers = {header[0]: header[1] for header in response_headers}
        return response_headers

    def get_current_url(self):
        """Gets the current url after redirect (if any).

        :return: String
        """
        return self.browser.current_url

    def get_page_source(self, url, **kwargs):
        """Returns page source of the url

        :param url: url to crawl
        :param kwargs:
                    - wait - wait time in seconds for the element in the web page.
                    - xpath - element to wait. If this parameter is not given, selenium will wait for the document
                                to be ready till wait time.

        :return: HTML Web page string
        """
        self.fetch(url, **kwargs)
        return self.browser.page_source

    def clean_up(self):
        """quits browser and sets None, when this method is called"""
        self.browser.quit()
        self.browser = None

    @classmethod
    def get_executable_path(cls, browser, **kwargs):
        """Gets browser executable from repository using `webdriver_manager`.

        :param browser: name of the browser
        :param kwargs: webdriver_manager options for the browser to download executable.
        :return: BrowserDriver
        """
        if browser == ChromeType.GOOGLE:  # noqa
            return ChromeDriverManager(**kwargs).install()
        elif browser == "FIREFOX":  # noqa
            return GeckoDriverManager(**kwargs).install()
        else:
            raise BrowserNotSupportedError(browser)
