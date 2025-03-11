from flask import Flask
from flask_alembic import Alembic
from flask_sqlalchemy import SQLAlchemy

from app.models.base import Base
from config.config import Config
from app.api.routes import api_bp

app = Flask(__name__)
app.config.from_object(Config())

db = SQLAlchemy(model_class=Base)

alembic = Alembic(metadatas=Base.metadata)

db.init_app(app)
alembic.init_app(app)
    
app.register_blueprint(api_bp, url_prefix="/api")
    