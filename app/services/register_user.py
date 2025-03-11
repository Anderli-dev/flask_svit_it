from flask import Response, make_response
from flask_jwt_extended import create_access_token
from app.models.user import User
from app import db
from app.schemas.Token import TokenSchema
from app.schemas.User import UserSchema
from app.utils.hash_password import hash_password

token_schema = TokenSchema()

def register_user(data: dict) -> Response:
    if User.query.filter_by(username=data['username']).first():
        return make_response({"error": 'User already exists'}, 400)
            
    user: User = User(username=data['username'], password_hash=hash_password(data['password']))
    
    db.session.add(user)
    db.session.commit()
    
    access_token: str = create_access_token(identity=user.username)
    
    return make_response(token_schema.jsonify({"access_token": access_token}))