from flask import Response, jsonify, request, make_response
from flask_restful import Resource
from marshmallow import ValidationError

from app.schemas.User import UserAuthenticationSchema
from app.services.register_user import register_user

user_auth_schema = UserAuthenticationSchema()

class Register(Resource):
    def post(self) -> Response:
        try:
            data: dict = user_auth_schema.load(data=request.json)
            if not data:
                return make_response({"message": "No input data provided"}, 400)
            
            register_user_response: Response = register_user(data)

            return register_user_response
        
        except ValidationError as err:
            return make_response(jsonify({"error": err.messages}), 400)
        except Exception as e:
            return make_response({"message": f"An error occurred: {str(e)}"}, 500)