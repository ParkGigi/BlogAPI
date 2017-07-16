import pymysql
from flask import Flask


api = Flask(__name__)
api.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

db = pymysql.connect(host='localhost',
                     user='root',
                     db='blog')
