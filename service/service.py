import sys

sys.path.append("..")

from dao import dao
from entity import entity
from utils import error

class UserService(object):
    def __init__(self):
        self._dao = dao.UserDao()


    def create_user(self, user):
        if not isinstance(user, entity.User):
            raise TypeError("Must be of type user")
        if self._dao.get(user.id) is None:
            self._dao.put(user)
        else:
            raise error.UserAlreadyExists()

    def delete_user(self, user_id):
        pass


    def update_user(self, user_id, user):
        if not isinstance(user, entity.User):
            raise TypeError("Must be of type user")
        pass

    def get_all_users(self):
        pass


if __name__ == "__main__":
    service = UserService()
