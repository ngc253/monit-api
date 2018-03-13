import hashlib
import uuid

from extensions import db


class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(256), unique=True)
    is_ldap = db.Column(db.Boolean())
    is_local = db.Column(db.Boolean())
    salt = db.Column(db.String(32))

    def __init__(self, username='root', password='root', email='root@gmail.com', is_ldap = False, is_local=True):
        self.username = username
        self.salt = uuid.uuid4().hex
        self.password = hashlib.sha256(password + self.salt).hexdigest()
        self.email = email
        self.is_ldap = is_ldap
        self.is_local = is_local
