import bcrypt

from api import db

def get():
    users = []
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Users;")
    for user_id, username, password, nickname, picture, user_level, delete, created, updated  in cursor.fetchall():
        users.append(
            {
                "id": user_id,
                "username": username,
                "password": password,
                "picture": picture,
                "user_level": user_level,
                "delete": delete,
                "created": created,
                "updated": updated,
            }
        )
        cursor.close()
    return users


def get_one_user(username):
    user_information = {}
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Users WHERE username=%s;", (username, password))
    result = cursor.fetchone()
    user_information = {
        "id": result[0],
        "username": result[1],
        "password": result[2],
        "nickname": result[3],
        "picture": result[4],
        "user_level": result[5],
        "delete": result[6],
        "created": result[7],
        "updated": result[8]
    }
    cursor.close()
    return user_information

def get_user_id(username):
    cursor = db.cursor()
    cursor.execute("SELECT id FROM USERS WHERE username=%s;", (username,))
    user_id = cursor.fetchone()[0]
    cursor.close()
    return user_id

def validate(username, password):
    cursor = db.cursor()
    cursor.execute("SELECT password FROM Users WHERE username=%s;", (username,))
    result = cursor.fetchone()
    cursor.close()

    if result:
        fetched_password = result[0]
    else:
        return False

    return bcrypt.checkpw(password.encode(), fetched_password)
