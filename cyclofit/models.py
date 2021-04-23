from cyclofit import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    profile = db.relationship('Profile', backref='user', uselist=False)
    # console-print
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.password}')"

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(20), nullable=False)
    contact_no = db.Column(db.Integer, unique=True, nullable=False)
    dob = db.Column(db.String(20), nullable=False)
    emergency_no = db.Column(db.Integer, unique=True, nullable=False)
    date_registered = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)
    # console-print
    def __repr__(self):
        return f"User('{self.area}', '{self.contact_no}', '{self.dob}', '{self.emergency_no}', '{self.date_registered}')"