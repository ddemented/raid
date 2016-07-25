from raid import raid
from flask import render_template
from models import User


# use decorators to link the function to a url
@raid.route('/')
def home():
    return render_template('index.html', page='home')

@raid.route('/login')
def login():
    return render_template('login.html', page='login')  # render a template

@raid.route('/register')
def register():
    return render_template('login.html', page='register')

@raid.route('/about-us')
def about():
    return render_template('about-us.html', page='about-us')

@raid.route('/contact-us')
def contact():
    return render_template('contact-us.html', page='contact-us')

#@raid.route('/testdb')
#def testdb():
#  return User.query.all()

