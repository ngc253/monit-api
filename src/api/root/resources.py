
from flask_restful import Resource

from src.extensions import db
from src.models.user import User


class RootResource(Resource):
    def get(self):
        return {
            "msg": "success"
        }, 200


class SampleResource(Resource):
    def get(self):
        user = User()
        db.session.add(user)
        db.session.commit()
        return {
            "msg": "success"
        }, 200