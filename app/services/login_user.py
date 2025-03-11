from flask import Response, make_response
from flask_jwt_extended import create_access_token
from app.models.user import User
from app.schemas.Token import TokenSchema
from app.utils.hash_password import verify_password

token_schema = TokenSchema()


def login_user(data: dict) -> Response:
    user: User = User.query.filter_by(username=data['username']).first()
    if user is None:
            return make_response({'error': 'User not found'}, 404)
    
    if verify_password(data['password'], user.password_hash):
        access_token: str = create_access_token(identity=user.username)

        return make_response(token_schema.jsonify({"access_token": access_token}))
    else:
        return make_response({'error': 'Invalid credentials'}, 401)