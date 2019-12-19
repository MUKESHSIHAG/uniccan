from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message = 'Please log in to access this page.'
bootstrap = Bootstrap(app)

db.init_app(app)
login_manager.init_app(app)

from app import models, routes