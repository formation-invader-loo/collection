from enum import Enum

class htmlErrorCode(Enum):
  InvalidArgumentException = 460
  CollectionAlreadyExists = 461
  CollectionDoesNotExist = 462
  DocumentAlreadyExists = 463
  DocumentDoesNotExist = 464


class InvalidArgumentException(Exception):
  """Exception raised for errors that are Caused if a invalid Argument was given.

  Attributes:
      message -- explanation of the error
  """

  def __init__(self, message):
    self.message = message
    self.error_no = htmlErrorCode.InvalidArgumentException
    super().__init__(self.message)


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


def raise_switch(err_no: int, msg: str) -> None:
  """Raises the Error Corresponding to the err_no given from a server response. If no err_no matches the function returns None.

  Args:
      err_no (int): html err_no defined in htmlErrorCode
      msg (str): description of the error

  Returns:
      None

  Raises:
      CollectionException.InvalidArgumentException: _description_
      CollectionException.CollectionAlreadyExists: _description_
      CollectionException.CollectionDoesNotExist: _description_
      CollectionException.DocumentAlreadyExists: _description_
      CollectionException.DocumentDoesNotExist: _description_
  """
  if err_no == htmlErrorCode.InvalidArgumentException:
    raise InvalidArgumentException(msg)
  elif err_no == htmlErrorCode.CollectionAlreadyExists:
    raise CollectionAlreadyExists(msg)
  elif err_no == htmlErrorCode.CollectionDoesNotExist:
    raise CollectionDoesNotExist(msg)
  elif err_no == htmlErrorCode.DocumentAlreadyExists:
    raise DocumentAlreadyExists(msg)
  elif err_no == htmlErrorCode.DocumentDoesNotExist:
    raise DocumentDoesNotExist(msg)
  else:
    return
