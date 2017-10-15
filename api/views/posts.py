from flask import request, redirect

from api import api
from api.data import users, posts, comments
from api.views.utility import jsonify, require_session


@api.route('/posts', methods=['GET'])
def posts_handler():
    return jsonify(posts.get())

@api.route('/posts', methods=['POST'])
def posts_create_handler():
    session, redirect = require_session()
    
    data = request.json
    
    post = posts.create(data)
    return jsonify(post)


@api.route('/posts/<post_id>', methods=['GET'])
def posts_get_one(post_id):
    print('post_id in views!!!',post_id)
    return jsonify(posts.get_one_post(post_id))

@api.route('/posts/<post_id>', methods=['PUT'])
def posts_update_handler(post_id):
    session, redirect = utility.require_session()
    #session, redirect = utility.require_session()
    #if redirect:
    #    return redirectbw
    data = request.json
    posts.update(post_id)
    return


@api.route('/posts/<post_id>', methods=['DELETE'])
def posts_delete_handler(post_id):
    session, redirect = utility.require_session()
    if posts.get_one(post_id):
        response_message = posts.delete(post_id)
        return jsonify({ "errors": [] })
    return jsonify({ "errors": ["Post does not exist."] })


@api.route('/posts/<post_id>/comments', methods=['POST'])
def write_comment_handler(post_id):
    session, redirect = utility.require_session()
    content = request.json
    result = comments.create(post_id, 1, content)
    return jsonify(result)


@api.route('/posts/<post_id>/comments', methods=['GET'])
def get_comment_handler(post_id):
    all_comments = comments.get(post_id)
    return jsonify(all_comments)


@api.route('/posts/<post_id>/comments/<comment_id>', methods=['DELETE'])
def delete_comment_handler(post_id, comment_id):
    # TODO: handle post_id too!
    session, redirect = utility.require_session()
    if comments.get_one(comment_id):
        response_message = posts.delete_comment(comment_id)
        return jsonify({ "errors": [] })
    return jsonify({"errors":["Comment does not exist."]})
