class InvalidResponseTypeError(Exception):
    def __init__(self, response_type):
        self.message = f"Invalid response type: {response_type}. only json and text are supported."


class CrawlerNotSupportedError(Exception):
    def __init__(self, name):
        self.message = f"Can not override default crawler {name}"


class ExecutorNotSupportedClientError(Exception):
    def __init__(self, name):
        self.message = f"Given executor {name} is not supported."
