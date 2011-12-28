from flask import Flask
app = Flask(__name__)

from lib.gzipper import Gzipper
app.wsgi_app = Gzipper(app.wsgi_app)

#import database
import view
#from views.module import module

#app.register_module(module, url_prefix='/path')
