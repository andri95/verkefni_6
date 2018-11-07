from sys import argv

import bottle
from bottle import *

bottle.debug(True)

@get('/')
def index():
    mynd1 = 'turn1.jpg'
    mynd2 = 'turn2.jpg'
    mynd3 = 'turn3.jpg'
    mynd4 = 'turn4.jpg'
    mynd5 = 'turn5.jpg'
    mynd6 = 'turn6.jpg'
    return template('index.tpl', mynd1 = mynd1, mynd2 = mynd2, mynd3 = mynd3, mynd4 = mynd4, mynd5 = mynd5, mynd6 = mynd6)

@route('/static/<filename>')
def send_image(filename):
    return static_file(filename, root='static')

bottle.run(host='0.0.0.0', port=argv[1])