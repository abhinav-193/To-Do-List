from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from sawo import createTemplate, getContext, verifyToken

db=SQLAlchemy()
DB_NAME = "database.db"

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = '9113304aamr'
    '''app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' '''
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jlvpgeokeyjtjt:08a34632ef4506eae7434bdaebea3168aea9b47d76fdfc6b725287a0dadf8556@ec2-3-218-71-191.compute-1.amazonaws.com:5432/d57hcgaiguqqem'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    '''postgres://jlvpgeokeyjtjt:08a34632ef4506eae7434bdaebea3168aea9b47d76fdfc6b725287a0dadf8556@ec2-3-218-71-191.compute-1.amazonaws.com:5432/d57hcgaiguqqem'''
    

    from .views import views
    from .auth import auth
    

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('webite/' + DB_NAME):
        db.create_all(app=app)
        print('<<Created Database>>')