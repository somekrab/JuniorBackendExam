import mysql.connector
from config import DB_CONFIG

class User:
    def __init__(self):
        self.conn = mysql.connector.connect(**DB_CONFIG) #Uses DB_CONFIG from config.py
        self.cursor = self.conn.cursor(dictionary=True)

    # Used for getting username
    def get_user_by_username(self, username):
        query = "SELECT * FROM users WHERE username = %s"
        self.cursor.execute(query, (username,))
        return self.cursor.fetchone()
    
    def insert_user(self, username, password, is_admin=False):
        try:
            self.cursor.execute(
                "INSERT INTO users (username, password, is_admin) VALUES (%s, %s, %s)",
                (username, password, is_admin)
            )
            self.conn.commit()
            return True
        except mysql.connector.Error as err:
            print("Error:", err)
            return False
        
    def get_non_admin_users(self):
        query = "SELECT username FROM users WHERE is_admin = FALSE"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        usernames = []
        for row in rows:
            usernames.append(row['username'])
        return usernames
        
    def get_all_users(self):
        self.cursor.execute("SELECT username, is_admin FROM users")
        rows = self.cursor.fetchall()
        return [{"username": row['username'], "is_admin": row['is_admin']} for row in rows]
        
    def close(self):
        self.cursor.close()
        self.conn.close()