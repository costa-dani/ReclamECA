from flask import Flask
from config import Config
from dynaconf import FlaskDynaconf

app = Flask(__name__)
app.config.from_object(Config)

FlaskDynaconf(app)

from app import routes, models