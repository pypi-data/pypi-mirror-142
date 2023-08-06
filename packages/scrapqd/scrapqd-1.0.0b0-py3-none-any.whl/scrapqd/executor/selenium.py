import json

from scrapqd.executor import logger
from scrapqd.executor.selenium_driver.factory import BrowserFactory
from scrapqd.fetch.interface import Executor


class Selenium(Executor):
    """SeleniumExecutor is class a generic processor (facade) for all browsers and
    implements all abstract method from `Executor` class."""

    def __init__(self, url, **kwargs):
        super().__init__(url, **kwargs)
        self._response_headers = {}
        self._current_url = None

    def get_response_url(self):
        if not self._current_url:
            logger.error("Not able to get current_url for %s from selenium", self.url, exc_info=True)
            return self.url
        return self._current_url

    def is_success(self):
        return True

    def get_response_text(self):
        return self.response

    def get_response_json(self):
        if isinstance(self.response, str):
            try:
                self.response = json.loads(self.response)
            except Exception:
                logger.exception("Not able to get convert to json data %s", self.url, exc_info=True)

        return self.response

    def get_status_code(self):
        return 200

    def get_response_headers(self):
        return self._response_headers

    def crawl(self, url, method="get", headers=None, **kwargs):
        """"Selenium crawl gets browser from browser factory and crawls the url"""
        browser_name = kwargs.get("browser", "GOOGLE_CHROME")
        browser = BrowserFactory().get(browser_name)()
        response = browser.get_page_source(url, **kwargs)
        self._response_headers = browser.get_response_headers()
        self._current_url = browser.get_current_url()
        return response
