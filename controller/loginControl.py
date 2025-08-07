from model.user import User

class LoginController:
    # Call Usermodel when initialized
    # Also performs SQL search
    def __init__(self):
        self.model = User()

    def login(self, username, password):
        user = self.model.get_user_by_username(username)
        if user and  user['password'] == password:
            return True
        return False

    def close(self):
        self.model.close()