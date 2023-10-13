from flask import Flask
from .ext import configuration
from .main import views
app = Flask(__name__)

views.init_app(app)
configuration.init_app(app)
