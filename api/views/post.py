from flask import jsonify

from api import api
from api.data import posts

@api.route('/posts')
def posts_handler():
    return jsonify(posts.get())
