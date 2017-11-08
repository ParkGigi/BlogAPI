import configparser
import sys
from subprocess import call

import pymysql
from flask import Flask


def is_testing():
    return 'unittest' in sys.argv[0]

def init_config():
    configuration = configparser.RawConfigParser()

    if is_testing():
        configuration.read('test.cfg')
    else:
        configuration.read('dev.cfg')
    return configuration

CONFIG = init_config()

api = Flask(__name__) # pylint: disable=invalid-name
api.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

def init_db():
    host = CONFIG.get('db', 'host')
    user = CONFIG.get('db', 'user')
    db_name = CONFIG.get('db', 'name')

    if is_testing():
        call(["mysql", "-u", user, '-e',
              """drop database if exists {};
              create database {};
              use {};
              source schema.sql;""".format(db_name, db_name, db_name)])
    return pymysql.connect(host=host, user=user, db=db_name)

db = init_db() #pylint: disable=invalid-name
