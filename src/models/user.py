
import datetime
import uuid

import jwt
from flask import current_app

from src.extensions import db, bcrypt


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(256), unique=True)
    is_ldap = db.Column(db.Boolean())
    is_local = db.Column(db.Boolean())
    salt = db.Column(db.String(32))
    is_admin = db.Column(db.Boolean())

    def __init__(self, username='root', password='root', email='root@gmail.com', is_ldap = False, is_local=True, is_admin=True):
        self.username = username
        self.salt = uuid.uuid4().hex
        self.password = bcrypt.generate_password_hash(password, current_app.config.get('BCRYPT_LOG_ROUNDS')).decode()
        self.email = email
        self.is_ldap = is_ldap
        self.is_local = is_local
        self.is_admin = is_admin

    @staticmethod
    def encode_auth_token(data):
        try:
            payload = {
                'exp': datetime.datetime.utcnow()  + datetime.timedelta(days=0, hours=1),
                'iat': datetime.datetime.utcnow(),
                'sub': data
            }
            return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')
        except Exception as e:
            return e


    @staticmethod
    def decode_auth_token(auth_token):
        try:
            if not BlacklistToken.is_token_blacklisted(auth_token):
                payload = jwt.decode(auth_token, current_app.config['SECRET_KEY'])
                return payload['sub']['username']
            else:
                return 'Token Blacklisted. Login again.'
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Login again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Login again'


class BlacklistToken(db.Model):
    __tablename__ = 'blacklist_tokens'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    token = db.Column(db.String(500), unique=True, nullable = False)
    blacklisted_on = db.Column(db.DateTime, nullable= False)

    def __init__(self, token):
        self.token = token
        self.blacklisted_on = datetime.datetime.utcnow()

    def __repr__(self):
        return '<id: token: {}'.format(self.token)

    @staticmethod
    def is_token_blacklisted(token):
        res = BlacklistToken.query.filter_by(token=str(token)).first()
        if res:
            return True
        else:
            return False
