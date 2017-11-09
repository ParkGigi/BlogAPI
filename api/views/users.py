from flask import request, redirect

from api import api
from api.data import users
from api.views.utility import jsonify

@api.route('/account/create', methods=['POST'])
def sign_up():
    data = request.get_json()
    create_account = users.create(data)
    return jsonify(create_account)

@api.route('/admin/login', methods=['POST'])
def log_in_post():
    data = request.get_json()
    print('In the view function!!!!!!')
    result = users.validate(data['username'], data['password'])
    print('This is result!!!!', result)
    if result:
        print('password passed!!!!!!!')
        return
    else:
        print('here!!!!!!!!!!')
        return redirect('/admin/login')

@api.route('/users', methods=['GET'])
def users_get():
    result = users.get()
    return jsonify(result)
