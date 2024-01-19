import os

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from server.auth.views import  UserListbyOne,UserRegistration, db
from dotenv import load_dotenv

load_dotenv()

# We have created an app instance
def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY")
    api = Api(app)
    db.init_app(app)
    
    jwt = JWTManager(app)
    
    with app.app_context():
        db.create_all()
    
    # register resources
    api.add_resource(UserRegistration, '/user/register')
    api.add_resource(UserListbyOne, '/user/<int:id>')
    
    return app
