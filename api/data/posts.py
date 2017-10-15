from api import db

def get():
    posts = []
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Posts;")
    #print(cursor.fetchall())
    for post_id, author_id, title, content, deleted, created, updated in cursor.fetchall():
        posts.append({
            "id": post_id,
            "author_id": author_id,
            "title": title,
            "content": content,
            "deleted": deleted,
            "created": created,
            "updated": updated,
        })
    cursor.close()
    return posts

def get_one_post(post_id):
    print('This is post_id: ', post_id)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Posts WHERE id=%s;", (post_id,))
    post_id, author_id, title, content, deleted, created, updated = cursor.fetchone()
    cursor.close()
    return {
        "id": post_id,
        "author_id": author_id,
        "title": title,
        "content": content,
        "deleted": deleted,
        "created": created,
        "updated": updated,
    }

def create(post_dictionary):
    post = {}
    cursor = db.cursor()

    if not post_dictionary['title'] or not post_dictionary['content']:
        return
    
    cursor.execute("INSERT INTO Posts (author_id, title, content) Values(%s, %s, %s)",(1, post_dictionary['title'], post_dictionary['content']))
    db.commit()
    last_id = cursor.lastrowid
    cursor.execute("SELECT * FROM Posts WHERE id=%s", (last_id,))
    post_info = cursor.fetchone()
    post = {
        "id": post_info[0],
        "author_id": post_info[1],
        "title": post_info[2],
        "content": post_info[3],
        "created": post_info[4],
        "updated": post_info[5]
    }
    cursor.close()
    return post

def update(post_id, title, content):
    response_message=""
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM Posts WHERE id=%s;",(post_id,))
        if cursor.fetchone():
            cursor.execute("UPDATE Posts SET title=%s, content=%s WHERE id=%s;",(title, content,))
            response_message="Posts id %s is updated" % post_id
        else:
            response_message="Posts id %s does not exist" % post_id
    cursor.close()
    return response_message

def delete(post_id):
    response_message=""
    cursor = db.cursor()
    cursor.execute("DELETE FROM Posts WHERE id=%s", (post_id,))
    cursor.close()    
    return response_message

def write_comment(post_id, commentor_id, content):
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

def get_all_comments(post_id):
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

def get_one_comment(comment_id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Comment WHERE id=%s", (comment_id,))
    comment_info = cursor.fetchone()
    return comment_info

def delete_comment(comment_id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM Comment WHERE id=%s", (comment_id,))
    db.commit()
    cursor.close()
    return
