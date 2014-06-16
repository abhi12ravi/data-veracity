
import sys
sys.path.append("../..")

import pymongo
import utils.config as config


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
        if username is None:
            db.authenticate(username, password=password)
        return db[collection_name]



class UserDao(object):
    def __init__(self):
        self._collection = MongoConnection.get_collection('User')

    def get(self, id):
        pass # todo

    def put(self, id):
        pass


class MetaDataDao(object):

    def __init__(self):
        pass # todo


    def get_meta_data(self, data):
        pass # todo

    def update_meta_data(self, meta_data):
        pass # todo



if __name__ == "__main__":
    user_dao = UserDao()
