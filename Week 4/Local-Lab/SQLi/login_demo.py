
import sqlite3

def unsafe_login(username, password):

    connection = sqlite3.connect("training.db")
    cursor = connection.cursor()

    # UNSAFE: User input is directly joined into SQL
    query = (
        "SELECT * FROM users WHERE username = '"
        + username
        + "' AND password = '"
        + password
        + "'"
    )

    print("\n[UNSAFE SQL QUERY]")
    print(query)

    cursor.execute(query)
    result = cursor.fetchone()

    connection.close()

    return result


def secure_login(username, password):

    connection = sqlite3.connect("training.db")
    cursor = connection.cursor()

    # SECURE: Parameters keep input separate from SQL commands
    query = """
    SELECT * FROM users
    WHERE username = ? AND password = ?
    """

    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    connection.close()

    return result


print("=== LOCAL SQL INJECTION TRAINING LAB ===")

username = input("Enter username: ")
password = input("Enter password: ")

print("\n--- Unsafe Login Result ---")

unsafe_result = unsafe_login(username, password)

if unsafe_result:
    print("Login successful!")
    print("User:", unsafe_result[1])
    print("Role:", unsafe_result[3])
else:
    print("Login failed!")

print("\n--- Secure Login Result ---")

secure_result = secure_login(username, password)

if secure_result:
    print("Login successful!")
    print("User:", secure_result[1])
    print("Role:", secure_result[3])
else:
    print("Login failed!")
