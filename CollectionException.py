from utils.htmlErrorCodes import htmlErrorCode

class CollectionAlreadyExists(Exception):
    """Exception raised for errors that are Caused if a Collection already exists.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        self.error_no = htmlErrorCode.CollectionAlreadyExists
        super().__init__(self.message)


class CollectionDoesNotExist(Exception):
    """Exception raised for errors that are Caused if a Collection does not exist.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        self.error_no = htmlErrorCode.CollectionDoesNotExist
        super().__init__(self.message)


class DocumentAlreadyExists(Exception):
    """Exception raised for errors that are Caused if a Document already exists.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        self.error_no = htmlErrorCode.DocumentAlreadyExists
        super().__init__(self.message)


class DocumentDoesNotExist(Exception):
    """Exception raised for errors that are Caused if a Document does not exist.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        self.error_no = htmlErrorCode.DocumentDoesNotExist
        super().__init__(self.message)
