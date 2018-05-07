from flask import Blueprint
from flask_restful import Api

bp = Blueprint('main', __name__)
api = Api(bp)

from app.main import routes
api.add_resource(routes.TodoItem, '/todos')
api.add_resource(routes.Portfolio, '/portfolio')

# from app.main import routes