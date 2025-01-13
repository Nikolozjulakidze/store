from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import json

with open('data/keys.json', 'r') as file:
    keys = json.load(file)

app = Flask(__name__)
app.config["SECRET_KEY"] = keys.get('secret_key')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"


db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"