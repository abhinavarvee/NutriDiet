import sqlite3
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login_user(username, password):
    if not username or not password:
        return False, "Please fill in both username and password fields."
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()

    hashed_password = hash_password(password)
    
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = c.fetchone()
    
    if user:
        stored_hashed_password = user[2]  
        if hashed_password == stored_hashed_password:
            return True, f"Logged in as: {username}"
        else:
            return False, "Incorrect password. Please try again."
    else:
        return False, "Username not found. Please register."

    conn.close()
