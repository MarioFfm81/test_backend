from models.userModel import UserModel

users = [
    UserModel(1, "user 1", "abc123"),
    UserModel(2, "user 2", "abc123")
]

def authenticate(username, password):
    for user in users:
        if user.username==username and password=="abc123":
            return user

def indentity(payload):
    user_id = payload['identity']
    for user in users:
        if user.id == user_id:
            return user
    