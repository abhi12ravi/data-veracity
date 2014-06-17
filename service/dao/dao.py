import sys

sys.path.append("../..")

import pymongo
import utils.config as config
from entity.entity import User
from entity.entity import Status


class MongoConnection(object):
    @staticmethod
    def get_collection(collection_name):
        configuration = config.Config()
        username = configuration.get_property('MONGO_USERNAME')
        password = configuration.get_property('MONGO_PASSWORD')
        host = configuration.get_property('MONGO_HOST')
        port = int(configuration.get_property('MONGO_PORT'))
        db_name = configuration.get_property('MONGO_DB_NAME')

        mongo_client = pymongo.MongoClient(host=host, port=port)
        db = mongo_client[db_name]
        if username is not None:
            db.authenticate(username, password=password)
        return db[collection_name]


class UserDao(object):
    def __init__(self):
        self._collection = MongoConnection.get_collection(User.conf.collection_name)

    def get(self, id):
        user_db_obj = self._collection.find_one({User.conf.id: id})
        if user_db_obj is not None:
            return User.get_user_from_db_object(user_db_obj)
        else:
            return None

    def put(self, user):
        json = user.json()
        if json is not None:
            self._collection.insert(json)

    def update(self, id, user):
        json = user.json()
        if json is not None:
            self._collection.update({User.conf.id: id}, json)

    def get_cursor(self):
        cursor = self._collection.find()
        for user in cursor:
            yield User.get_user_from_db_object(user)


if __name__ == "__main__":
    user_dao = UserDao()
    user1 = User(1)
    user2 = User(2)

    for user in user_dao.get_cursor():
        print user
