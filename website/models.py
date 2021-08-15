from enum import unique
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy import PickleType
from sqlalchemy.dialects.sqlite import BLOB
from flask import Flask, render_template, url_for
from sawo import createTemplate, getContext, verifyToken

class Pdf(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(100))
    data = db.Column(db.LargeBinary)
    description = db. Column(db.String(1000), default="None")
    branch = db.Column(db.String(1000), default="None")
    no_of_upvotes = db.Column(db.Integer, default= 0)
    


class User(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    
    
    pdf= db.relationship('Pdf', backref='author', lazy=True)

class Config(models.Models):
    api_key = models.CharField(max_length=200)
    identifier = models.CharField(max_length=200)
    choices = [("email","Email"),("phone_number_sms","Phone")]