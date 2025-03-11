from flask import Response, jsonify, make_response, request
from flask_restful import Resource
from marshmallow import ValidationError

from app.schemas.User import UserAuthenticationSchema
from app.services.login_user import login_user

user_auth_schema = UserAuthenticationSchema()

class Login(Resource):
    def post(self) -> Response:
        try:
            data: dict = user_auth_schema.load(data=request.json)
            if not data:
                return make_response({"message": "No input data provided"}, 400)
            
            login_user_response: Response = login_user(data)

            return login_user_response
        
        except ValidationError as err:
            return make_response(jsonify({"error": err.messages}), 400)
        except Exception as e:
            return make_response({"message": f"An error occurred: {str(e)}"}, 500)