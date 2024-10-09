from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Database Models
class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    staff_name = db.Column(db.String(100), nullable=False, unique=True)
    drink_tab = db.Column(db.Float, default=0.0)
    orders = db.relationship('DrinkOrder', backref='staff', lazy=True, cascade="all, delete-orphan")

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    drink_name = db.Column(db.String(100), nullable=False, unique=True)
    drink_cost = db.Column(db.Float, nullable=False)

class DrinkOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
    drink_id = db.Column(db.Integer, db.ForeignKey('drink.id'), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    drink = db.relationship('Drink')