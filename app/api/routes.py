from flask import Blueprint
from app.api.home import Home
from flask_restful import Api

from app.api.log import LogResource
from app.api.login import Login
from app.api.register import Register 

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Home, '/')
api.add_resource(Register, '/register')
api.add_resource(Login, '/login')

api.add_resource(LogResource, '/log')