from flask import Flask
from flask_sqlalchemy import SQLAlchemy

raid = Flask(__name__)
raid.config.from_pyfile('config.py')
raid.secret_key = 'secret'

db = SQLAlchemy(raid)

from raid import models, views
#class example(db.Model):
#    __tablename__ = 'example'
#    id = db.column(db.Integer, primary_key=True)
#    data = db.Column(db.Unicode)
    
