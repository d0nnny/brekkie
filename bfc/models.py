import string
from datetime import datetime
from random import choices
from .extensions import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    place_id = db.Column(db.Integer,  unique=True)
    owner_id = db.Column(db.Integer,  unique=True)


class OrderItem(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    place_item_id = db.Column(db.Integer,  unique=True)
    user_id = db.Column(db.String(64),  unique=True)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),  unique=True)
    email = db.Column(db.String(64),  unique=True)
    sms_number = db.Column(db.Integer,  unique=True)    


class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),  unique=True)


class PlaceItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    place_id = db.Column(db.Integer,  unique=True)    
    name = db.Column(db.String(64),  unique=True)    
    price = db.Column(db.Numeric,  unique=True)  # review   
