from flask import request, redirect

from api import api
from api.data import users
from api.views.utility import jsonify

@api.route('/users', methods=['GET'])
def users_handler():
    return jsonify(users.get())
