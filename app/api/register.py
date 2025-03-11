from flask import Response, jsonify, request, make_response
from flask_restful import Resource
from marshmallow import ValidationError

from app.schemas.User import UserLoginSchema, UserSchema
from app.utils.register_user import register_user


user_login_schema = UserLoginSchema()

class Register(Resource):
    def post(self) -> Response:
        try:
            data = user_login_schema.load(data=request.json)
            if not data:
                return make_response({"message": "No input data provided"}, 400)
            
            register_user_response: Response = register_user(data)

            return register_user_response
        
        except ValidationError as err:
            return make_response(jsonify({"error": err.messages}), 400)
        except Exception as e:
            return make_response({"message": f"An error occurred: {str(e)}"}, 500)