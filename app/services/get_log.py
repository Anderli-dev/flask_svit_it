import datetime

from flask import Response, make_response
from app.models.log import Log
from app.schemas.Log import LogSchema

logs_schema = LogSchema(many=True)

def get_log(from_time, to_time, keyword) -> Response:
    query = Log.query
            
    if from_time:
        from_time = datetime.datetime.strptime(from_time, '%Y-%m-%d %H:%M:%S')
        query = query.filter(Log.timestamp >= from_time)
    if to_time:
        to_time = datetime.datetime.strptime(to_time, '%Y-%m-%d %H:%M:%S')
        query = query.filter(Log.timestamp <= to_time)
    if keyword:
        query = query.filter(Log.content.contains(keyword))
    
    logs: list[Log]  = query.all()
    
    return make_response(logs_schema.jsonify(logs))