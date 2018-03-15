from flask import Blueprint, make_response, jsonify, request
from flask_restful import Api

from src.api.root.resources import RootResource, SampleResource
from src.models.user import User

api = Blueprint('api', __name__, url_prefix='/api/v1')

router = Api(api)

router.add_resource(RootResource, '/')
router.add_resource(SampleResource, '/sample/')


@api.before_request
def api_before_request():
    auth_header = request.headers.get('Authorization')
    auth_token = ''
    if auth_header:
        try:
            sp = auth_header.split(" ")
            if sp[0] != "Bearer":
                return make_response(
                    jsonify({
                        'status': 'fail',
                        'message': 'Invalid header format. Include Bearer before the token'
                    })
                ), 400
            if len(sp[1]) > 0:
                auth_token = sp[1]
        except IndexError:
            responseObject = {
                'status': 'fail',
                'message': 'Bearer token malformed.'
            }
            return make_response(jsonify(responseObject)), 401

    if auth_token:
        resp = User.decode_auth_token(auth_token)
        if isinstance(resp, str):
            user = User.query.filter_by(username=resp).first()
            if not user:
                responseObject = {
                    'status': 'fail',
                    'message': resp
                }
                return make_response(jsonify(responseObject)), 401

        else:
            responseObject = {
                'status': 'fail',
                'message': 'Bearer token malformed. username not found on decode'
            }
            return make_response(jsonify(responseObject)), 401

    else:
        responseObject = {
            'status': 'fail',
            'message': 'Auth token is empty'
        }
        return make_response(jsonify(responseObject)), 401
