


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




class Status(object):

    def __init__(self,id):
        self._id = id
        self._tags = {}
        self._content = None


    @property
    def id(self):
        return self._id

    @property
    def content(self):
        return self._content

    @property
    def tags(self):
        return self._tags.copy()

    @content.setter
    def content(self, value):
        self._content = value

    @property
    def tag_count(self, tag):
        if tag in self._tags.keys():
            return self._tags[tag]
        else:
            return 0

    def increment_tag(self, tag):
        if tag in self._tags.keys():
            self._tags[tag] += 1
        else:
            self._tags[tag] = 1

    def update_tag(self, tag, value):
        self._tags[tag] = value

if __name__ == "__main__":
    # Test Cases for User
    user = User(52)
    assert user.id == 52

    user.add_status(1)
    assert 1 in user.get_statuses()

    user.remove_status(1)
    assert 1 not in user.get_statuses()

    status = Status(52)

    assert status.id == 52

