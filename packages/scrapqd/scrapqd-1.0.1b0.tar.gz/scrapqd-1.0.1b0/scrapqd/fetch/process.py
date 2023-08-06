import copy

from scrapqd.fetch.exception import (ExecutorNotSupportedClientError,
                                     InvalidResponseTypeError)
from scrapqd.fetch.factory import ExecutorFactory


class Process:
    """Facade and Factory class to access the various crawlers seemingly"""

    def __init__(self, url, executor="request", method="get", headers=None, response_type="text", **kwargs):
        """Create process instance for executor

        :param url: URL to crawl
        :param executor: Crawl request will be processed using the given executor.
                         System uses "requests" library as default executor.
        :param method: Http method which should be used to crawl
        :param headers: Additional headers for executor. Some websites need addition headers to make request.
                        System add below request headers by default. These headers can be overridden using
                        header argument.

                        - User-Agent: from the data files.
                        - Connection: keep-alive
                        - Upgrade-Insecure-Requests: 1
                        - Accept-Language: en-US,en;q=0.9
                        - Accept-Encoding: gzip, deflate, br
                        - Pragma: no-cache
        :param response_type: Expected response format.
                              Valid Formats:

                                - json
                                - text
        :param kwargs: Additional keyword arguments to support executor.
        :raises InvalidResponseTypeError: Raises when unsupported response type is provided.
        """
        _options = copy.deepcopy(kwargs)
        self.url = url
        self.executor = executor
        self.method = method
        self.headers = {} if headers is None else headers
        self.response_type = response_type
        self.options = _options
        self._processor = "NA"

        if response_type.lower() not in ["json", "text"]:
            raise InvalidResponseTypeError(response_type)

    @property
    def processor(self):
        """Factory method to get executor based on executor"""
        if self._processor == "NA":
            _executor_cls = ExecutorFactory().get(self.executor)
            if not _executor_cls:
                raise ExecutorNotSupportedClientError(self.executor)
            _executor_instance = _executor_cls(url=self.url,
                                               method=self.method,
                                               headers=self.headers,
                                               response_type=self.response_type)
            self._processor = _executor_instance
        return self._processor

    def crawl(self):
        """Calls execute method of the executor with extra options"""
        self.processor.execute(**self.options)
        return self.processor
