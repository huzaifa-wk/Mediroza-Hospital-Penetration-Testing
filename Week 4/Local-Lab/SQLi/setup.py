
import sqlite3

# Create a local training database
connection = sqlite3.connect("training.db")

cursor = connection.cursor()

# Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL
)
""")

# Clear old training records
cursor.execute("DELETE FROM users")

# Insert fictional training accounts
users = [
    ("admin", "Admin123!", "admin"),
    ("employee", "User123!", "employee"),
    ("student", "Student123!", "student")
]

cursor.executemany(
    "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
    users
)

connection.commit()
connection.close()

print("Training database created successfully!")
print("3 fictional users added.")
