class hcordException(Exception):
    """Base class for every errors in hcord."""


class Forbidden(hcordException):
    def __init__(self, message=None):
        if message is None:
            super().__init__()
        super().__init__(message)


class NotFound(hcordException):
    def __init__(self, message=None):
        if message is None:
            super().__init__()
        super().__init__(message)


class HTTPException(hcordException):
    def __init__(self, message=None):
        if message is None:
            super().__init__()
        super().__init__(message)


class NotAllowedIntents(hcordException):
    def __init__(self, message=None):
        if message is None:
            super().__init__()
        super().__init__(message)


class HasntStartedYet(hcordException):
    def __init__(self, message=None):
        if message is None:
            super().__init__()
        super().__init__(message)


class NotImportable(hcordException):
    def __init__(self, message=None):
        if message is None:
            super().__init__()
        super().__init__(message)
