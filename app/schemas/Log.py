from app import ma
from app.models.log import Log


class LogSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Log
        load_instance = True
