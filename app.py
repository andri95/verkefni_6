
from sys import argv

import bottle
from bottle import *

bottle.debug(True)

@get('/')
def index():
    return template("index.tpl")

@route('/static/<filename:re:.*\jpg>')
def send_image(filename):
    return static_file(filename, root='static')

bottle.run(host='0.0.0.0', port=argv[1])