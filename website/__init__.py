from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app(): 
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Xxnezsrcn7Aw@'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://rkqwdpakvbeemb:1b988f69b178f28e8c00e59c0959352b178a5cb6b3409c53fe289493d223458a@ec2-34-198-186-145.compute-1.amazonaws.com:5432/d56qajvnl83ooj'
    db.init_app(app)


    #blueprints for website
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id): 
        return User.query.get(int(id))

    return app 


def create_database(app): 
    if not path.exists('website/' + DB_NAME): 
        db.create_all(app=app)
        print('Baza de date creata!')