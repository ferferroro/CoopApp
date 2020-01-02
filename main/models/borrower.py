from main import db
from datetime import datetime

class Borrower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(50), unique=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    address = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    mobile = db.Column(db.String(50))
    email = db.Column(db.String(50))
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)
    interest_rate = db.Column(db.Float)
    penalty_rate = db.Column(db.Float)
    balance = db.Column(db.Float)