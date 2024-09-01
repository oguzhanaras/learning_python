import sqlite3


def show_users():
    conn = sqlite3.connect("user_info.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    user_list = cursor.fetchall()
    conn.close()
    return user_list


for user in show_users():
    id, username, email, age = user
    print(username, email, age)