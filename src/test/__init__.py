from flask import Blueprint
from flask_restful import Api

from src.api.root.resources import SampleResource

testapi = Blueprint('test', __name__, url_prefix='/test')

router = Api(testapi)

router.add_resource(SampleResource, '/create_root_user')