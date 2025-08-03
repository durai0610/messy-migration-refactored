from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import DATABASE_URL

db = SQLAlchemy()

def init_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app
