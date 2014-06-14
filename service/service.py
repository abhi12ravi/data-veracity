
from ..data_veracity import data_veracity

class UserService(object):

    def __init__(self):
        pass


    def add_new_user(self,user):
        if not isinstance(user, entity.User):
            raise TypeError("Must be of type user")


if __name__ == "__main__":
    service = UserService()
    service.add_new_user(list())
