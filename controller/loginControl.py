from model.user import User
import hashlib

class LoginController:
    # Call Usermodel when initialized
    # Also performs SQL search
    def __init__(self):
        self.model = User()

    # Hashes password with SHA256
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    # Login
    def login(self, username, password):
        user = self.model.get_user_by_username(username)
        # Hashes input to compare with database entry
        hashed_input = self.hash_password(password)

        # Verifies input
        if user and user['password'] == hashed_input:
            # returns user as a dictionary (with column data)
            return user
        return None

    def close(self):
        self.model.close()