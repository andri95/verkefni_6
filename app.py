<<<<<<< HEAD
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

import bottle
from bottle import *

bottle.debug(True)

@get('/')
def index():
    return "Hallo Heimur í Heroku og Github"

bottle.run(host='0.0.0.0', port=argv[1])
=======
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

import bottle
from bottle import *

bottle.debug(True)

@get('/')
def index():
    return "Hallo Heimur í Heroku og Github"

bottle.run(host='0.0.0.0', port=argv[1])
>>>>>>> d076964670b766777b4fe2452c571604a22d5c72
