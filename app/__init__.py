from flask import Flask

from app.utils.db import db
from config.config import Config
from app.api.routes import api_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    
    db.init_app(app)

    app.register_blueprint(api_bp, url_prefix="/api")

    return app