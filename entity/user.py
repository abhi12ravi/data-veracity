


class User(object):

    def __init__(self, id):
        self._id = id
        self._status_ids = set()

    @property
    def id(self):
        return self._id

    def add_status(self, id):
        self._status_ids.add(id)

    def remove_status(self, id):
        if id in self._status_ids:
            self._status_ids.remove(id)

    def get_statuses(self):
        return self._status_ids.copy()

    def json(self):
        jsonMap = {}
        jsonMap["_id"] = self._id
        jsonMap["statuses"] = self._status_ids
        return jsonMap


if __name__ == "__main__":
    user = User(52)
    assert user.id == 52

    user.add_status(1)
    assert 1 in user.get_statuses()
