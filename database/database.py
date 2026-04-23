import sqlite3
import os

# Dynamic path so the database stays in your project folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "users.db")

def create_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Create a table for users
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_user(fname, lname, pword):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO users (firstname, lastname, password) 
            VALUES (?, ?, ?)
        ''', (fname, lname, pword))
        conn.commit()
        return True
    except Exception as e:
        print(f"Database Error: {e}")
        return False
    finally:
        conn.close()

# Run this once to create the file
if __name__ == "__main__":
    create_db()
    print("Database and Table created successfully!")