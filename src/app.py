import os

from flask import Flask

from src.api import api
from src.auth import auth
from src.extensions import db, bcrypt
from src.test import testapi


def create_app():
    ap = Flask(__name__)
    configure_app(ap)
    configure_ext(ap)
    register(ap)
    return ap

def configure_app(ap):
    settings = os.getenv('APP_SETTINGS', 'src.config.DevConfig')
    ap.config.from_object(settings)

def configure_ext(ap):
    db.init_app(ap)
    bcrypt.init_app(ap)

def register(ap):
    ap.register_blueprint(auth)
    ap.register_blueprint(api)
    ap.register_blueprint(testapi)
