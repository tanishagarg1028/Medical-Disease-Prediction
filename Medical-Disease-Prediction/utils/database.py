import sqlite3, os
DB_PATH="database/medical.db"
def get_connection():
 os.makedirs("database",exist_ok=True)
 return sqlite3.connect(DB_PATH)
def initialize_database():
 conn=get_connection();c=conn.cursor();c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT)");c.execute("CREATE TABLE IF NOT EXISTS predictions(id INTEGER PRIMARY KEY AUTOINCREMENT, patient TEXT, disease TEXT, doctor TEXT, created_at TEXT)");conn.commit();conn.close()
