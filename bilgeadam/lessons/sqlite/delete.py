import sqlite3


def delete_user(user_id):
    conn = sqlite3.connect("user_info.db")
    cursor = conn.cursor()
    query = "DELETE FROM users WHERE id = ?"
    parameters = (user_id,)
    cursor.execute(query, parameters)
    conn.commit()
    conn.close()
    print("kayıt slindi")
    return True


delete_user(1)