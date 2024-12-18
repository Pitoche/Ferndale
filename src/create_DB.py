import sqlite3
import os

# Define the database file path
db_path = "/home/angel/ADL-TOOL/ADL-TOOL-DB.db"

# Check if the database exists; if not, create it
if not os.path.exists(db_path):
    # Connect to the SQLite database (this creates the file if it doesn't exist)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create a table to store user data
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Insert a 'tester' user with password 'tester'
    cursor.execute('''
        INSERT INTO users (username, password)
        VALUES (?, ?)
    ''', ('tester', 'tester'))

    # Create the vulnerabilities table with the necessary columns
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vulnerabilities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            version TEXT NOT NULL,
            vulnerability_id TEXT NOT NULL,
            fix_version TEXT,
            skip_reason TEXT,
            type TEXT NOT NULL DEFAULT 'PIP-AUDIT'
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print("Database created successfully with 'tester' user and updated 'vulnerabilities' table.")
else:
    print(f"Database already exists at {db_path}")
