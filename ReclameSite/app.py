from flask import Flask
from main import views
from ext import configuration

app = Flask(__name__)

configuration.init_app(app)
views.init_app(app)