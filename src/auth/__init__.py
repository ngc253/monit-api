from flask import Blueprint, request, jsonify

from src.extensions import bcrypt
from src.models.user import User

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/login', methods=['POST'])
def login():
    """
    Validate users and generate auth and refresh tokens

    :return: json string
    """
    if not request.is_json:
        return jsonify({
            "msg": "Missing username and password"
        }), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    print request.json
    if not username or not password:
        return jsonify({
            "msg": "Username or password cannot be empty"
        }), 400

    user = User.query.filter_by(username=username).first()

    if user is None or not bcrypt.check_password_hash(user.password, password):
        return jsonify({
            "msg": "Bad credentials"
        }), 400

    token = User.encode_auth_token({
        "username": user.username
    })

    print User.decode_auth_token(token)

    return jsonify({
        "token": token
    }), 200

