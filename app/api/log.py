from flask import Response, make_response, request
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from app.services.get_log import get_log
from app.utils.archive_handler import ArchiveHandler
from app.utils.read_log import read_log


class LogResource(Resource):
    @jwt_required()
    def get(self) -> Response:
        try:
            from_time: str = request.args.get('from_time')
            to_time: str = request.args.get('to_time')
            keyword: str = request.args.get('keyword')
            
            logs_response: Response = get_log(from_time, to_time, keyword)
            
            return logs_response
        except Exception as e:
            return make_response({"message": f"An error occurred: {str(e)}"}, 500)
        
    @jwt_required()
    def post(self) -> Response:
        try:
            if 'file' not in request.files:
                return {'message': 'No file part'}, 400
            
            file = request.files['file']
            
            handler = ArchiveHandler() # a special class for handling different types of files
            extracted_path = handler.process_file(file) # a function that starts processing
            
            read_log(extracted_path) # reading and writing the log to the database
            
            return make_response({'message': 'File uploaded successfully'})
        except Exception as e:
            return make_response({"message": f"An error occurred: {str(e)}"}, 500)