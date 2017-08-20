from flask import make_response, request, redirect

from api.data import sessions
import datetime
import json

def jsonify(obj):
    def jsonify_dict(d):
        for key, val in d.items():
            if isinstance(val, bytes):
                d[key] = val.decode()
            elif isinstance(val, datetime.datetime):
                d[key] = val.isoformat()
        return d

    if isinstance(obj, dict):
        obj = jsonify_dict(obj)
    elif isinstance(obj, list):
        obj = list(map(jsonify_dict, obj))

    return json.dumps(obj)

def get_session():
    session_id = request.cookies.get('session_id')
    if not session_id:
        return False

    session = sessions.get(session_id)

    if (not session or session['expired']):
        return False

    return session

def set_session(response, session_id):
    response = make_response(response)
    response.set_cookie('session_id', str(session_id).encode())
    return response

# session, redirect = require_session()
# if redirecT:
#   return redirect
# blah blah blah
def require_session():
    session = get_session()
    if session:
        return session, None
    return None, redirect('/login')
