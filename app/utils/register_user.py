from flask import Response, make_response
from app.models.user import User
from app import db
from app.schemas.User import UserSchema
from app.utils.hash_password import hash_password

user_schema = UserSchema()

def register_user(data: dict) -> Response:
    if User.query.filter_by(username=data['username']).first():
        return make_response({"error": 'User already exists'}, 400)
            
    user = User(username=data['username'], password_hash=hash_password(data['password']))
    
    db.session.add(user)
    db.session.commit()
    
    return make_response(user_schema.jsonify(user), 200)