import hashlib

from extensions import jwt
from models.user import User
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_refresh_token_required, get_jwt_identity

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
    if user is None or hashlib.sha256(password + user.salt).hexdigest() != user.password:
        return jsonify({
            "msg": "Bad credentials"
        }), 400

    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)
    ret = {
        'access_token': access_token,
        'refresh_token': refresh_token
    }

    return jsonify(ret), 200


@auth.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    """
    Refresh auth token

    :return: json
    """
    current_user = get_jwt_identity()
    ret = {
        'access_token': create_access_token(identity=current_user)
    }

    return jsonify(ret), 200



@jwt.user_loader_callback_loader
def user_loader_callback(identity):
    """
    User loader callback

    :param identity: integer
    :return: user object
    """
    return User.query.get(identity)