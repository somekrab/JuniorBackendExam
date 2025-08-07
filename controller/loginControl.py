from model.user import User
import hashlib

class LoginController:
    # Call Usermodel when initialized
    # Also performs SQL search
    def __init__(self):
        self.model = User()

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def login(self, username, password):
        user = self.model.get_user_by_username(username)
        hashed_input = self.hash_password(password)

        if user and user['password'] == hashed_input:
            return user
        return None

    def add_user(self, username, password, is_admin=False):
        if self.model.get_user_by_username(username):
            return False
        hashed_pw = self.hash_password(password)
        self.model.insert_user(username, hashed_pw, is_admin)
        return True

    def close(self):
        self.model.close()