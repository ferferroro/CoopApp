from main import db
# from sqlalchemy.dialects.postgresql import UUID
import uuid

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(50), unique=True)
    company_name = db.Column(db.String(50))
    address = db.Column(db.String(100))
    phone = db.Column(db.String(50))
    mobile = db.Column(db.String(50))
    total_fund = db.Column(db.Float)
    available_fund = db.Column(db.Float)
    lended_fund = db.Column(db.Float)
    total_profit = db.Column(db.Float)
    interest_rate = db.Column(db.Float)

