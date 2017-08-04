import configparser
import sys
from subprocess import call

import pymysql
from flask import Flask


def is_testing():
    return 'unittest' in sys.argv[0]

def init_config():
    config = configparser.RawConfigParser()

    if is_testing():
        config.read('test.cfg')
    else:
        config.read('dev.cfg')
    return config

config = init_config()

api = Flask(__name__)
api.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

def init_db():
    host = config.get('db', 'host')
    user = config.get('db', 'user')
    db = config.get('db', 'name')

    if is_testing():
        r = call(["mysql", "-u", user, '-e', 'drop database if exists {}; create database {}; use {}; source schema.sql;'.format(db, db, db)])

    return pymysql.connect(host=host, user=user, db=db)

db = init_db()
