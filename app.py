from sys import argv

import bottle
from bottle import *

bottle.debug(True)

@get('/')
def index():
    return template ('index.tpl')

bottle.run(host='0.0.0.0', port=argv[1])