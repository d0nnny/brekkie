import string
from datetime import datetime
from .extensions import db
from .auth import requires_aut



class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    details = db.Column(db.Text)
    time_placed = db.Column(db.DateTime, default=datetime.now)
    orderitem = db.relationship('OrderItem', backref='order')
    Delivery = db.relationship('Delivery', backref='order') # case sensitive ?

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer,db.ForeignKey('order.id'))
    menuitem_id = db.Column(db.Integer,db.ForeignKey('menuitem.id'))


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64),  unique=True, nullable=False)
    email = db.Column(db.String(64),  unique=True, nullable=False)
    sms_number = db.Column(db.Integer,  unique=True, nullable=False)   
    join_date = db.Column(db.DateTime, default=datetime.now)
    order = db.relationship('Order', backref='customer') # uesList useList=False



class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),  unique=True)
    description = db.Column(db.String(64))
    menuitems = db.relationship('MenuItem', backref='menu') # lazy parameter
    

class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'), nullable=False)
    item_name = db.Column(db.String(64),  unique=True)
    item_description = db.Column(db.Text)
    item_photo = db.Column(db.Text)
    orderitem = db.relationship('OrderItem', backref='menuitem')

class Delivery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer,db.ForeignKey('order.id'))
    customer_id = db.Column(db.Integer,db.ForeignKey('customer.id'))
    delivery_man_id = db.Column(db.Integer,db.ForeignKey('delivery_man.id'))
    


class Delivery_Man(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64),  unique=True, nullable=False)
    email = db.Column(db.String(64),  unique=True, nullable=False)
    sms_number = db.Column(db.Integer,  unique=True, nullable=False)    
    Delivery = db.relationship('devlivery', backref='delivery_man')