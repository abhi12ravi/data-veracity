import sys

sys.path.append("..")

from dao import dao
from entity import entity
from utils import error


class UserService(object):
    def __init__(self):
        self._dao = dao.UserDao()

    @staticmethod
    def type_check(user):
        if not isinstance(user, entity.User):
            raise TypeError("Must be of type User")

    def create_user(self, user):
        UserService.type_check(user)
        if self._dao.get(user.id) is None:
            self._dao.put(user)
        else:
            raise error.UserAlreadyExists()

    def delete_user(self, user_id):
        self._dao.remove(user_id)

    def update_user(self, user_id, user):
        UserService.type_check(user)
        self._dao.update(user)

    def get_all_users(self):
        return self._dao.get_cursor()

    def add_status_to_user(self, user_id, status_id):
        user = self._dao.get(user_id) # todo



class StatusService(object):

    def __init__(self):
        self._dao = dao.StatusDao()

    @staticmethod
    def type_check(status):
        if not isinstance(status, entity.Status):
            raise TypeError("Must by of type Status")

if __name__ == "__main__":
    service = UserService()
