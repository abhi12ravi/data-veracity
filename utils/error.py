


class GenericError(Exception):
    pass

class UserAlreadyExists(GenericError):

    msg = "User Already Exists"

    def __str__(self):
        return self.msg

class StatusDoesNotExist(GenericError):
    pass
