import sqlite3
import os

# Finds the database folder
DB_FOLDER = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(DB_FOLDER, "nona_users.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                      (firstname TEXT, lastname TEXT, password TEXT)''')
    conn.commit()
    conn.close()

def signup_user(fn, ln, pw):
    if not fn or not pw: return False
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users VALUES (?, ?, ?)", (fn, ln, pw))
    conn.commit()
    conn.close()
    return True

def login_user(username, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE firstname=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None

init_db()