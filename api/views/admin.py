from flask import request, render_template, redirect, make_response, send_from_directory

from api import api
from api.data import sessions
from api.views import utility


@api.route('/admin')
def show_admin():
    session, redirect = utility.require_session()
    return render_template('admin.html')


@api.route('/admin/login')
def display_example():
    if utility.get_session():
        return redirect('/admin')
    return render_template('index.html')


@api.route('/admin/login', methods=['POST'])
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
