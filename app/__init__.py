from flask import Flask
from config import Config
from dynaconf import FlaskDynaconf

app = Flask(__name__)
app.config.from_object(Config)
FlaskDynaconf(app)

db = 3
from app import routes, models