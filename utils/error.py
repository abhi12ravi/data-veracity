


class GenericError(Exception):
    msg = "Generic Error"

    def __str__(self):
        return "Exception: {}, Message:{}".format(self.__class__.__name__, self.msg)

class UserAlreadyExists(GenericError):
    msg = "User Already Exists"


class StatusDoesNotExist(GenericError):
    msg = "Status Does not Exist"
