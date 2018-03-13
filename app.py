from api.views import api
from auth.views import auth
from extensions import db, jwt
from flask import Flask


def create_app(filename='config.py'):
    app = Flask(__name__)
    configure_app(app, filename)
    configure_ext(app)
    register(app)
    return app

def configure_app(app, filename):
   app.config.from_pyfile(filename)

def configure_ext(app):
    db.init_app(app)
    jwt.init_app(app)

def register(app):
    app.register_blueprint(auth)
    app.register_blueprint(api)