from api import db

def get():
    posts = []
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM Post;")
    for post_id, author_id, title, content, created, updated in cursor.fetchall():
        posts.append({
            "id": post_id,
            "author_id": author_id,
            "title": title.decode(),
            "content": content.decode(),
            "created": created,
            "updated": updated,
        })
    cursor.close()
    return posts
