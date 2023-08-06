class InvalidParserError(NotImplementedError):
    def __init__(self, parser):
        self.message = f"Invalid parser - {parser} is not implemented"


class InvalidParserArgumentsError(Exception):
    def __init__(self):
        self.message = "Parser instance can not be created without raw_html or html_tree."


class ParserUnavailableError(Exception):
    def __init__(self):
        self.message = "parser is empty document."


class RawDatatypeNotSupportedError(Exception):
    def __init__(self, data_type):
        self.message = f"User defined '{data_type}' data conversion is not supported."


class InvalidDataTypeError(NotImplementedError):
    def __init__(self, key, data_type):
        self.message = f"Invalid datatype: {key} - {data_type}"


class LeafNotSupportedError(Exception):
    def __init__(self, name):
        self.message = f"Can not override default leaf {name}"


class QueryFieldNotSupportedError(Exception):
    def __init__(self, name):
        self.message = f"Can not override default query field {name}"
