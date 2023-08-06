class BrowserNotSupportedConfigError(Exception):
    def __init__(self, name):
        self.message = f"Can not override default browser {name}"


class BrowserNotSupportedError(Exception):
    def __init__(self, name):
        self.message = f"Given browser {name} is not supported by system."
