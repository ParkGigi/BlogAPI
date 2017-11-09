from flask import request, render_template, redirect

from api import api
from api.data import sessions, users
from api.views import utility


@api.route('/admin/')
def admin():
    _, returned_redirect = utility.require_session()
    if returned_redirect:
        return returned_redirect
    return render_template('admin.html')

@api.route('/admin/login')
def login_get():
    if utility.get_session():
        return redirect('/admin')
    return render_template('admin.html')


@api.route('/admin/login', methods=['POST'])
def login_post():
    username = request.get_json().get('username')
    password = request.get_json().get('password')

    errors = []

    if not username:
        errors.append({'field': 'username', 'message': 'Must supply username'})

    if not password:
        errors.append({'field': 'password', 'message': 'Must supply password'})

    if errors:
        return utility.jsonify({'errors': errors})

    print(username, password)
    if not users.validate(username, password):
        return utility.jsonify({
            'errors': [
                {'field': '', 'message': 'Username or password is invalid'}
            ]
        })

    session_id = sessions.create(username)
    return utility.set_session(utility.jsonify({'errors': []}), session_id)

@api.route('/admin/logout')
def logout():
    return utility.set_session(redirect('/admin'), None)
