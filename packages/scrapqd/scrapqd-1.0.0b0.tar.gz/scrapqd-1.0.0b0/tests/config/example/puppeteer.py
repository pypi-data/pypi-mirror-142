import requests

from scrapqd.fetch.interface import Executor


class Puppeteer(Executor):
    """Sample Puppeteer is created from requests executor"""

    def get_response_url(self):
        return self.response.url

    def get_response_headers(self):
        return dict(self.response.headers)

    def get_status_code(self):
        return self.response.status_code

    def get_response_text(self):
        return self.response.content

    def get_response_json(self):
        return self.response.json()

    def is_success(self):
        status_code = self.get_status_code()
        return status_code in self.success_status_code

    def crawl(self, url, method="get", headers=None, **kwargs):
        return requests.request(self.method, self.url, headers=headers, **kwargs)
