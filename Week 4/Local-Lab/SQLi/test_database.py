
import sqlite3

# Connect to our training database
connection = sqlite3.connect("training.db")
cursor = connection.cursor()

# Retrieve all users
cursor.execute("SELECT * FROM users")

# Fetch database records
users = cursor.fetchall()

# Display results
print("Users stored in database:")
print("-" * 40)

for user in users:
    print(user)

connection.close()
