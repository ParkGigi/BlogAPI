from flask import request, render_template, redirect, make_response

from api import api
from api.data import users, posts, comments, sessions
from api.views import utility

@api.route('/posts', methods=['GET'])
def posts_handler():
    return utility.jsonify(posts.get())

@api.route('/posts', methods=['POST'])
def posts_create_handler():
    session, redirect = utility.require_session()
    
    data = request.json
    
    post = posts.create(data)
    return utility.jsonify(post)

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
        return utility.jsonify({ "errors": [] })
    return utility.jsonify({ "errors": ["Post does not exist."] })

@api.route('/posts/<post_id>/comments', methods=['POST'])
def write_comment_handler(post_id):
    session, redirect = utility.require_session()
    content = request.json
    result = comments.create(post_id, 1, content)
    return utility.jsonify(result)

@api.route('/posts/<post_id>/comments', methods=['GET'])
def get_comment_handler(post_id):
    all_comments = comments.get(post_id)
    return utility.jsonify(all_comments)

@api.route('/posts/comments/<comment_id>', methods=['DELETE'])
def delete_comment_handler(comment_id):
    session, redirect = utility.require_session()
    if comments.get_one(comment_id):
        response_message = posts.delete_comment(comment_id)
        return utility.jsonify({ "errors": [] })
    return utility.jsonify({"errors":["Comment does not exist."]})

@api.route('/login')
def display_example():
    if utility.get_session():
        return redirect('/admin')
    return render_template('index.html')

@api.route('/login', methods=['POST'])
def receive_credentials():
    username = request.json.get('username')
    password = request.json.get('password')

    errors = []

    if not username:
        errors.append({ field: 'username', message: 'Must supply username'})

    if not password:
        errors.append({ field: 'password', message: 'Must supply password' })

    if errors:
        return utility.jsonify({ 'errors': errors })

    if not users.validate(username, password):
       return utility.jsonify({ 'errors': [{ field: '', message: 'Username or password is invalid' }] })
   
    session_id = sessions.create(username)

    return utility.set_session(utility.jsonify({ 'errors': [] }), session_id)

@api.route('/admin')
def show_admin():
    session, redirect = utility.require_session()
    print('Arrived at admin')
    return render_template('/admin.html')
