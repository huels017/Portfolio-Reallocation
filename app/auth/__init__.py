from flask import Blueprint
from flask_restful import Api

bp = Blueprint('auth', __name__)
api = Api(bp)

from app.auth import routes
api.add_resource(routes.Login, '/login')

# from app.auth import routes