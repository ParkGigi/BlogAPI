import bcrypt

from api import db

def get(username):
    user_information = {}
    curosr = db.cursor()
    cursor.execute("SELECT * FROM Users WHERE username=%s", (username, password))
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
