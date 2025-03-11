
from flask import Response, jsonify, make_response
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from marshmallow import ValidationError


class Log(Resource):
    @jwt_required()
    def get(self) -> Response:
        try:
            pass
        
        except ValidationError as err:
            return make_response(jsonify({"error": err.messages}), 400)
        except Exception as e:
            return make_response({"message": f"An error occurred: {str(e)}"}, 500)
        
    @jwt_required()
    def post(self) -> Response:
        try:
            pass
        
        except ValidationError as err:
            return make_response(jsonify({"error": err.messages}), 400)
        except Exception as e:
            return make_response({"message": f"An error occurred: {str(e)}"}, 500)