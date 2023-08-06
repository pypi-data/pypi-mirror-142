class InvalidParserObjectError(NotImplementedError):
    def __init__(self):
        self.message = f"Not able to parser object."
