from marshmallow import fields, validate
from app import ma

class UserSchema(ma.Schema):
    id = fields.Int()
    username = fields.Str()
    
class UserLoginSchema(ma.Schema):
    username = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    password = fields.Str(required=True,  validate=validate.Length(min=6))