from abc import ABC, abstractmethod

from scrapqd.fetch import logger


def get_user_agent():
    """gets random user agent"""
    from scrapqd.fetch.ua import get_user_agent as get_ua
    user_agent = get_ua()
    return user_agent


class Executor(ABC):
    """Interface for Executor implementation

    This class is exported only to assist people in implementing their own executors for crawling
    without duplicating too much code.
    """

    def __init__(self, url, method="get", headers=None, response_type=None):
        """creates executor instance

        :param url: url to crawl
        :param method: http method which should be used to crawl
        :param headers: additional headers for executor. Some websites need addition headers to make request.
                        System add below request headers by default. These headers can be overridden using
                        header argument.
                        1. User-Agent: from the data files.
                        2. Connection: keep-alive
                        3. Upgrade-Insecure-Requests: 1
                        4. Accept-Language: en-US,en;q=0.9
                        5. Accept-Encoding: gzip, deflate, br
                        5. Pragma: no-cache
        :param response_type: expected response format.
                              Valid Formats:
                                1. json
                                2. text
        """
        if headers is None:
            headers = {}
        self.url = url
        self.headers = headers
        self.method = method
        self.response_type = response_type
        self.response = None
        self._success_status_code = [200]

    def __init_subclass__(cls, **kwargs):
        """Registers executor when inherits `Executor` class"""
        super().__init_subclass__(**kwargs)
        parent_method_docstr = {}
        for i, v in Executor.__dict__.items():
            if v and callable(v) and v.__doc__ is not None:
                parent_method_docstr[i] = v.__doc__

        for i, v in cls.__dict__.items():
            if v and callable(v) and v.__doc__ is None and i in parent_method_docstr:
                v.__doc__ = parent_method_docstr[i]

    @property
    def success_status_code(self):
        """Default success code for the request. Default success codes are [200].

        :return: List
        """

        return self._success_status_code

    def get_payload(self, payload):
        """Creates payload for http request.

        :param payload: additional payload argument for request.
        :return: Dict
        """
        return {"json": payload}

    def get_default_headers(self):
        """Get user-agent and constructs other default headers for the request.

        :return: Dict
        """
        ua = get_user_agent()
        default_headers = {
            "User-Agent": ua,
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Pragma": "no-cache",
        }
        return default_headers

    def get_content_type_mapping(self):
        content_type_mapping = {
            "text/html; charset=UTF-8": "html"
        }
        return content_type_mapping

    def get_response_type(self):
        """Gets response type from the request response.

        :return: String
        """
        content_type_mapping = self.get_content_type_mapping()
        response_headers = self.get_response_headers()
        content_type = response_headers.get("Content-Type")
        response_type = content_type_mapping.get(content_type)
        return response_type

    def get_headers(self):
        """Constructs headers to be applied to the request from default headers and user provided headers.
        User provided headers will override default headers.

        :return: Dict
        """
        default_headers = self.get_default_headers()
        headers = {**default_headers, **self.headers}
        return headers

    def get_response_content(self):
        """gets response content from processed request.

        :return: json - if the response type is json
                 html - if the response type is text/html
        """
        response_content_type = self.get_response_type()
        response_type = self.response_type or self.get_response_type()
        content = self.get_response_json() if response_type == "json" else self.get_response_text()
        logger.debug("%s response type is %s. Given response type is %s",
                     self.url,
                     response_content_type,
                     self.response_type)

        return content

    def execute(self, **kwargs):
        """Executes crawl method and gets http response from web.

        :param kwargs: additional keyword arguments for extensibility.
        :raises Exception: re-raises the exception occurred in the block for client to capture and handle
        """
        try:
            payload = kwargs.pop("payload", None)
            if self.method.lower() == "post" and payload:
                kwargs["json"] = payload

            headers = self.get_headers()

            # TODO: Convert generic response to response class
            self.response = self.crawl(url=self.url,
                                       method=self.method,
                                       headers=headers,
                                       **kwargs)

            status_code = self.get_status_code()
            if not self.is_success():
                logger.warning("response code is %s, Failed to fetch %s \n%s",
                               status_code,
                               self.url,
                               self.response,
                               exc_info=True)
            else:
                logger.debug("response code is %s for url: %s", status_code, self.url)
        except Exception as e:
            logger.exception("Failed to fetch %s", self.url, exc_info=True)
            raise e

    @abstractmethod
    def get_response_url(self):
        """Gets response url. It should be the final url after redirect (if any).

        :return: String
        """

    @abstractmethod
    def get_response_headers(self):
        """Gets http response headers

        :return: Dict
        """

    @abstractmethod
    def is_success(self):
        """Method definition to identify the request is successful or not.
        By default, status_code == 200 is considered as success.

        :return: Boolean
        """

    @abstractmethod
    def get_response_text(self):
        """Gets response text.

        :return: String
        """

    @abstractmethod
    def get_response_json(self):
        """Gets response as json.

        :return: Dict
        """

    @abstractmethod
    def get_status_code(self):
        """Gets response status code of the http request made.

        :return: integer
        """

    @abstractmethod
    def crawl(self, url, method="get", headers=None, **kwargs):
        """Crawls given url from web. This method should return only http response from the library
        without any further processing of the response.

        :param url: url to crawl
        :param method: http method which should be used to crawl
        :param headers: additional headers for executor. Some websites need addition headers to make request.
                        System add below request headers by default. These headers can be overridden using
                        header argument.
                        1. User-Agent: from the data files.
                        2. Connection: keep-alive
                        3. Upgrade-Insecure-Requests: 1
                        4. Accept-Language: en-US,en;q=0.9
                        5. Accept-Encoding: gzip, deflate, br
                        5. Pragma: no-cache
        :param kwargs: additional keyword arguments to support executor.
        :return: http response
        """
