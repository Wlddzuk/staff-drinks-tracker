from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from models import db, Staff, Drink, DrinkOrder
from routes import bp as routes_bp


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///staff_drinks.db'  # your config
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional, to suppress warnings


db.init_app(app)

with app.app_context():
    db.create_all()  # Create database tables

app.register_blueprint(routes_bp)

if __name__ == '__main__':
    app.run(debug=True)