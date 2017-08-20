from api import db

def create(post_id, commentor_id, content):
    cursor = db.cursor()
    cursor.execute("INSERT INTO Comment (post_id, commentor_id, content) VALUES (%s, %s, %s)", (post_id, commentor_id, content['content']))
    last_id = cursor.lastrowid
    db.commit()
    cursor.execute("SELECT * FROM Comment WHERE id=%s", (last_id,))
    comment_info = cursor.fetchone()
    cursor.close()
    comment = {
        "id" : comment_info[0],
        "post_id" : comment_info[1],
        "commentor_id" : comment_info[2],
        "content" : comment_info[3],
        "created" : comment_info[4],
        "updated" : comment_info[5]
    }
    return comment

def get(post_id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Comment WHERE post_id=%s", (post_id,))
    all_comments = []
    for comment_id, post_id, commentor_id, content, created, updated  in cursor.fetchall():
        all_comments.append({
            'id': comment_id,
            'post_id': post_id,
            'commentor_id': commentor_id,
            'content': content,
            'cretaed': created,
            'updated': updated
        })
    cursor.close()
    return all_comments

def get_one(comment_id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Comment WHERE id=%s", (comment_id,))
    comment_info = cursor.fetchone()
    return comment_info

def delete(comment_id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM Comment WHERE id=%s", (comment_id,))
    db.commit()
    cursor.close()
    return

