import string
from datetime import datetime
from .extensions import db
from .auth import requires_auth
from random import choices 


class BreakfastOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    breakfast_id = db.Column(db.iInteger, db.ForeignKey('breakfast.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    details = db.Column(db.Text)
    time_placed = db.Column(db.DateTime, default=datetime.now)
    breakfastorderitem = db.relationship('breakfastorderitem', backref='breakfastorder')


class BreakfastOrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    breakfast_order_id = db.Column(db.Integer,db.ForeignKey('breakfast-order_id'))
    menuitem_id = db.Column(db.Integer,db.ForeignKey('menuitem.id'))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64),  unique=True, nullable=False)
    sms_number = db.Column(db.String(64),  unique=True, nullable=False)
    join_date = db.Column(db.DateTime, default=datetime.now)
    user_runner_id = db.Column(db.String(3), unique=True,nullable=False)
    breakfastorder = db.relationship('breakfastorder', backref='user')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.runner_id = self.generate_runner_id()
   
    def generate_runner_id(self):
        characters = string.digits + string.ascii_letters
        user_runner_id = ''.join(choices(characters, k=4))

        user = self.query.filter_by(user_runner_id=user_runner_id).first()
 
        if user:
            self.runner_id = self.generate_runner_id()

        return self.generate_runner_id()


class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),  unique=True)
    description = db.Column(db.String(64))
    menuitems = db.relationship('menuitems', backref='menu') # lazy parameter


class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'), nullable=False)
    item_name = db.Column(db.String(64),  unique=True)
    item_description = db.Column(db.Text)
    item_photo = db.Column(db.Text)
    orderitem = db.relationship('OrderItem', backref='menuitem')
    breakfastorderitem = db.relationship('breakfastorderitem', backref='menuitem')


class Breakfast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_runner_id = db.Column(db.String(3), db.ForeignKey('user.id'), nullable=False)
    menuitem_id = db.Column(db.Integer,db.ForeignKey('menuitem.id'))
    date = db.Column(db.DateTime, default=datetime.now,nullable=False) 
    breakfastorder = db.relationship('breakfastorder', backref='breakfast')