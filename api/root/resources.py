from extensions import db
from models.user import User
from flask_jwt_extended import jwt_required
from flask_restful import Resource


class RootResource(Resource):

    @jwt_required
    def get(self):
        # user = User()
        # db.session.add(user)
        # db.session.commit()
        return {
            'Monit Manager API ROOT': {
                'Available CRUD endpoints': [
                    {'name': 'auth', 'url': '/api/auth'}
                ]
            }
        }