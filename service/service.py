import sys

sys.path.append("..")

from dao import dao
from entity import entity
from utils import error


class UserService(object):
    def __init__(self):
        self._dao = dao.UserDao()

    @staticmethod
    def _check_user(user):
        if not isinstance(user, entity.User):
            raise TypeError("Must be of type user")

    def create_user(self, user):
        UserService._check_user(user)
        if self._dao.get(user.id) is None:
            self._dao.put(user)
        else:
            raise error.UserAlreadyExists()

    def delete_user(self, user_id):
        self._dao.remove(user_id)

    def update_user(self, user_id, user):
        UserService._check_user(user)
        self._dao.update(user_id,user)

    def get_all_users(self):
        return self._dao.get_cursor()

    def add_status_to_user(self, user_id, status_id):
        user = self._dao.get(user_id)


if __name__ == "__main__":
    service = UserService()
