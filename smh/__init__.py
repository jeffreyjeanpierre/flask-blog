#initialize the app and database instances
import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

#initialize authentication packages
from flask.ext.login import LoginManager

lm = LoginManager()
lm.session_protection = 'strong'
lm.login_view = 'auth.login'
lm.init_app(app)

#initialize the controllers and db models
from smh import views
from smh.models.models import *

#initialize other routes blueprints
from .auth import auth as auth_blueprint

app.register_blueprint(auth_blueprint, url_prefix='/auth')