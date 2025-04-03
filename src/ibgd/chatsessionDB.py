import sqlite3
from datetime import datetime

class ChatSessionDB:
    def __init__(self, db_path='chat_sessions.db'):
       
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.create_table()
        
    def create_table(self):
       
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS chat_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT,
                message TEXT,
                response TEXT,
                timestamp TEXT
            )
        ''')
        self.connection.commit()
        
    def log_request(self, session_id, message, response):
       
        timestamp = datetime.now().isoformat()
        self.cursor.execute('''
            INSERT INTO chat_sessions (session_id, message, response, timestamp)
            VALUES (?, ?, ?, ?)
        ''', (session_id, message, response, timestamp))
        self.connection.commit()
        
    def close(self):
        self.connection.close()