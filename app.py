from sys import argv

import bottle
from bottle import *

bottle.debug(True)

@get('/')
def index():
    return "virkar þetta"

bottle.run(host='0.0.0.0', port=argv[1])