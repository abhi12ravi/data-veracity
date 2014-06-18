# ######################SET CONFIGS HERE###########################
config = {
    # MONGO CONFIG
    "MONGO_USERNAME": None,
    "MONGO_PASSWORD": None,
    "MONGO_HOST": "localhost",
    "MONGO_PORT": 27017,
    "MONGO_DB_NAME": "DataVeracity",
    # USER COLLECTION CONFIG
    "USER_ID": "_id",
    "USER_COLLECTION": "User",
    "USER_FIELD_STATUS": "status_ids",
    # STATUS COLLECTION CONFIG
    "STATUS_COLLECTION": "Status",
    "STATUS_ID": "_id",
    "STATUS_TAGS": "tags",
    "STATUS_CONTENT": "content"
}
#################################################################


class Config(object):
    def __init__(self):
        self._config = config

    def get_property(self, property_name):
        if property_name not in self._config.keys():
            return None
        return self._config[property_name]


class MongoConfig(Config):
    @property
    def host(self):
        return self.get_property('MONGO_HOST')

    @property
    def port(self):
        return self.get_property('MONGO_PORT')

    @property
    def username(self):
        return self.get_property('MONGO_USERNAME')

    @property
    def db_name(self):
        return self.get_property('MONGO_DB_NAME')

    @property
    def password(self):
        return self.get_property('MONGO_PASSWORD')


class UserConfig(Config):
    @property
    def id(self):
        return self.get_property('USER_ID')

    @property
    def status_ids(self):
        return self.get_property('USER_FIELD_STATUS')

    @property
    def collection_name(self):
        return self.get_property('USER_COLLECTION')


class StatusConfig(Config):
    @property
    def id(self):
        return self.get_property('STATUS_ID')

    @property
    def collection_name(self):
        return self.get_property('STATUS_COLLECTION')

    @property
    def tags(self):
        return self.get_property('STATUS_TAGS')

    @property
    def content(self):
        return self.get_property('STATUS_CONTENT')


if __name__ == "__main__":
    conf = Config()
    print conf.get_property()
    print int(conf.get_property('MONGO_PORT'))
    print conf.get_property('MONGO_USERNAME')
    print conf.get_property('MONGO_PASSWORD')
    print conf.get_property('MONGO_DB_NAME')

    user_conf = UserConfig()
    print user_conf.id
    print user_conf.status_ids
    print user_conf.collection_name