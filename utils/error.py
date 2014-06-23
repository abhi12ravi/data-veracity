


class GenericError(Exception):
    pass

class UserAlreadyExists(GenericError):
    pass


class StatusDoesNotExist(GenericError):
    pass
