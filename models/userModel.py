class UserModel():

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
        

    @classmethod
    def all(cls):
        return self.users

    @classmethod
    def find_by_id(cls, _id):
        for user in cls.users:
            if user['id'] == _id:
                return user
        return None

    @classmethod
    def find_by_username(cls, username):
        for user in cls.users:
            print(user)
            if user['name'] == username:
                return user
        return None