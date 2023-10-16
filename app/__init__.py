from flask import Flask
from config import Config
from dynaconf import FlaskDynaconf
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

FlaskDynaconf(app)


from app import routes, models