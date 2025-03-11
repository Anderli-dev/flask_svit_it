import datetime
from app import db

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.now)
    content = db.Column(db.Text, nullable=False)