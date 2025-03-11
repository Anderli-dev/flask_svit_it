
import os
import tarfile
import zipfile
from flask import Response, jsonify, make_response, request
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from marshmallow import ValidationError
from app.utils.archive_handler import ArchiveHandler
from app.utils.read_log import read_log

class LogResource(Resource):
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
            if 'file' not in request.files:
                return {'message': 'No file part'}, 400
            
            file = request.files['file']
            
            handler = ArchiveHandler()
            extracted_path = handler.process_file(file)
            
            read_log(extracted_path)
            
            return {'message': 'File uploaded successfully'}
        
        except ValidationError as err:
            return make_response(jsonify({"error": err.messages}), 400)
        except Exception as e:
            return make_response({"message": f"An error occurred: {str(e)}"}, 500)