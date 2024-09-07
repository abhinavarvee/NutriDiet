import sqlite3
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    if not username or not password:
        return False, "Please fill in both username and password fields."
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    
    hashed_password = hash_password(password)
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        conn.close()
        return True, f"Registered user: {username}"
    except sqlite3.IntegrityError:
        conn.close()
        return False, "Username already exists. Please choose a different one."
