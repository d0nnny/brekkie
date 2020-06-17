from flask import Blueprint, render_template, request, redirect
from .extensions import db

from .models import Order
from .models import OrderItem
from .models import Customer
from .models import Menu
from .models import MenuItem
from .models import Delivery
from .models import Delivery_Man
from .auth import requires_auth
# Request object - needed for servers's response to HTTP request

short = Blueprint('short', __name__)

@short.route('/')
@short.route('/order')
def index():
   return render_template('index.html')


@app.route('menus/id')
@app.route('/menus/<id>/items')
def showMenu(menu_id):
  menu = session.query(Menu).filter_by(id=menu_id).one()
  items = session.query(MenuItem).filter_by(menu_id=menu_id)
  return render_template('menu.html')

"""
@short.route('/menu_list', methods=['POST'])
#@requires_auth
def add_link():
    original_url = request.form['original_url']
    link = Link(original_url=original_url)
    db.session.add(link)
    db.session.commit()
    #request.form: the key/value pairs in the body, from a HTML post form, or JavaScript request that isn't JSON encoded
    
    return render_template('link_added.html', 
        new_link=link.short_url, original_url=link.original_url)
"""




@short.errorhandler(404)
def page_not_found(e):
    #return '<h1>404</h1>', 404 
    return render_template('4004.html'), 404