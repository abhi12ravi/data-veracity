
#######################SET CONFIGS HERE###########################
config = {
"MONGO_USERNAME" : None,
"MONGO_PASSWORD" : None,
"MONGO_HOST" : "localhost",
"MONGO_PORT"  : 27017,
"MONGO_DB_NAME" : "DataVeracity",
}

#################################################################

class Config(object):


    def __init__(self):
        self._config = config

    def get_property(self, property_name):
        if property_name not in self._config.keys():
            return None
        return self._config[property_name]


if __name__ =="__main__":
    conf = Config()
    print conf.get_property('MONGO_HOST')
    print int(conf.get_property('MONGO_PORT'))
    print conf.get_property('MONGO_USERNAME')
    print conf.get_property('MONGO_PASSWORD')
    print conf.get_property('MONGO_DB_NAME')