from flask import Blueprint, render_template, request, redirect
from .extensions import db

from .models import Order
from .models import OrderItem
from .models import Customer
from .models import Menu
from .models import MenuItem
from .models import Delivery
from .models import Delivery_Man


# Request object - needed for servers's response to HTTP request

short = Blueprint('short', __name__)

@short.route('/')
@short.route('/order')
def index():
    return render_template('index.html')

@short.route('/add_link', methods=['POST'])
@requires_auth
def add_link():
    original_url = request.form['original_url']
    link = Link(original_url=original_url)
    db.session.add(link)
    db.session.commit()
    #request.form: the key/value pairs in the body, from a HTML post form, or JavaScript request that isn't JSON encoded
    
    return render_template('link_added.html', 
        new_link=link.short_url, original_url=link.original_url)

@short.route('/stats')
#@requires_auth
def stats():
    links = Link.query.all()

    return render_template('stats.html', links=links)


@short.errorhandler(404)
def page_not_found(e):
    #return '<h1>404</h1>', 404 
    return render_template('4004.html'), 404