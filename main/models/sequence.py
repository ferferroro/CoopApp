from main import db
import uuid

class Sequence(db.Model):
    uuid = db.Column(db.UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    prefix = db.Column(db.String(10), unique=True)
    increment = db.Column(db.Integer)
    current = db.Column(db.Integer)