from marshmallow import fields
from app import ma

class TokenSchema(ma.Schema):
    access_token = fields.Str()