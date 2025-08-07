from model.user import User
import hashlib

class addUser:
    def __init__ (self, model):
         self.model = model

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()   
      
    def add_user(self, username, password, is_admin=False):
            if self.model.get_user_by_username(username):
                return False
            hashed_pw = self.hash_password(password)
            self.model.insert_user(username, hashed_pw, is_admin)
            return True
    
    def close(self):
        self.model.close()