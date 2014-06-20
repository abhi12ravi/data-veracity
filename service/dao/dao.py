import sys

sys.path.append("../..")

import pymongo
import utils.config as config
from entity.entity import User
from entity.entity import Status


class MongoConnection(object):
    @staticmethod
    def get_collection(collection_name):
        configuration = config.MongoConfig()
        mongo_client = pymongo.MongoClient(host=configuration.host, port=configuration.port)
        db = mongo_client[configuration.db_name]
        if configuration.username is not None:
            db.authenticate(configuration.username, password=configuration.password)
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

    def update(self, user):
        json = user.json()
        if json is not None:
            self._collection.update({
                                    User.conf.id: user.id
                                    }, json)

    def remove(self, id):
        self._collection.remove({User.conf.id: id})

    def get_cursor(self):
        cursor = self._collection.find()
        for user in cursor:
            yield User.get_user_from_db_object(user)

    def add_status(self,user_id, status_id):
        self._collection.update({
                                User.conf.id: user_id
                                },
                                {
                                '$addToSet':
                                    {User.conf.status_ids: status_id}
                                })

    def remove_status(self, user_id, status_id):
        self._collection.update({
                                User.conf.id: user_id
                                },
                                {
                                '$pull':
                                    {User.conf.status_ids: status_id}
                                })



class StatusDao(object):

    def __init__(self):
        self._collection = MongoConnection.get_collection(Status.conf.collection_name)


    def put(self, status):
        json = status.json()
        if json is not None:
            self._collection.insert(json)

    def get(self, status_id):
        status_db_object = self._collection.find_one({Status.conf.id : status_id})
        if status_db_object is not None:
            return Status.get_status_from_db_object(status_db_object)
        else:
            return None

    def remove(self, status_id):
        self._collection.remove({Status.conf.id:status_id})

    def get_cursor(self):
        cursor = self._collection.find()
        for object in cursor:
            yield Status.get_status_from_db_object(object)

    def set_tag(self, status_id, tag, tag_count):
        self._collection.update({
                                    Status.conf.id: status_id
                                },
                                {
                                    "$set" : { "{}.{}".format(Status.conf.tags,tag) : tag_count }
                                }
        )

    def remove_tag(self, status_id, tag):
        self._collection.update({
                                    Status.conf.id : status_id
                                },
                                {
                                    "$unset" : {"{}.{}".format(Status.conf.tags,tag):1}
                                }
        )

    def update(self, status):
        json = status.json()
        if json is not None:
            self._collection.update({
                Status.conf.id : status.id
            }, json)


if __name__ == "__main__":
    user_dao = UserDao()
    user1 = User(1)
    user2 = User(2)
    user_dao.remove_status(1,2 )
    for user in user_dao.get_cursor():
        print user

    status_dao = StatusDao()
    status1 = Status(232)
    status1.content = "This is a sample status"
    status1.update_tag("happy", 232)
    status1.update_tag("blah", 12)
    #status_dao.put(status1)
    status_dao.set_tag(232, 'freaky', 2323)
    #status_dao.remove_tag(232, 'mum')
