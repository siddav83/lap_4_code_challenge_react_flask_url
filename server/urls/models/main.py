from ..database.db import db

class Url(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    long_url = db.Column(db.String(50))
    short_url = db.Column(db.String(30))