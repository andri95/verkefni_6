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
    if request.query.item == "turnkassi1" or request.query.item == "turnkassi2" or request.query.item == "turnkassi3" or request.query.item == "turnkassi4" or request.query.item == "turnkassi5" or request.query.item == "turnkassi6:":
        product = request.query.item
        response.set_cookie("vara", product)
        return redirect('/')

    else:
        return template('index.tpl', mynd1 = mynd1, mynd2 = mynd2, mynd3 = mynd3, mynd4 = mynd4, mynd5 = mynd5, mynd6 = mynd6)


@get('/skodad')
def skodad():
    if request.get_cookie("vara"):
        valin_vara = request.get_cookie("vara")

    return template('skodad.tpl', valin_vara = valin_vara)


@route('/static/<filename>')
def send_image(filename):
    return static_file(filename, root='static')

bottle.run(host='0.0.0.0', port=argv[1])