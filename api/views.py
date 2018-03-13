from api.root.resources import RootResource
from flask import Blueprint
from flask_restful import Api

api = Blueprint('api', __name__, url_prefix='/api/v1')

router = Api(api)

router.add_resource(RootResource, '/')
