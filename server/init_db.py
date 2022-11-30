from urls import db
from urls import app

with app.app_context():
    db.drop_all()
    db.create_all()