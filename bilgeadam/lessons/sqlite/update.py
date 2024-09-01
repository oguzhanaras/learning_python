import sqlite3


def update_user(user_id, new_username, new_email, new_age):
    conn = sqlite3.connect("user_info.db")
    cursor = conn.cursor()
    sql_query = """
        UPDATE users
        SET username = ?, email = ?, age = ?
        WHERE id = ?
    """
    parameters = (new_username, new_email, new_age, user_id)
    cursor.execute(sql_query, parameters)
    conn.commit()
    conn.close()
    print("kayıt guncellendi")
    return True


update_user(5, "rafasilva", "silva@bjk.com", 36)