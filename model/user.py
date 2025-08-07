import mysql.connector
from config import DB_CONFIG

class User:
    def __init__(self):
        self.conn = mysql.connector.connect(**DB_CONFIG) #Uses DB_CONFIG from config.py
        self.cursor = self.conn.cursor(dictionary=True)

    def get_user_by_username(self, username):
        query = "SELECT * FROM users WHERE username = %s"
        self.cursor.execute(query, (username,))
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.conn.close()