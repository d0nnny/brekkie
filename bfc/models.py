import string
from datetime import datetime
from random import choices
from .extensions import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    place_id = db.Column(db.Integer, index=True, unique=True)
    owner_id = db.Column(db.Integer, index=True, unique=True)


class OrderItem(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    place_item_id = db.Column(db.Integer, index=True, unique=True)
    user_id = db.Column(db.String(64), index=True, unique=True)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True)
    sms_number = db.Column(db.Integer, index=True, unique=True)    


class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)


class PlaceItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    place_id = db.Column(db.Integer, index=True, unique=True)    
    name = db.Column(db.String(64), index=True, unique=True)    
    price = db.Column(db.Numeric, index=True, unique=True)  # review   