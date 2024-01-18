import os

from flask import Flask
from flask_restful import Api
from server.auth.views import UserRegistration, db
from dotenv import load_dotenv

load_dotenv()

# We have created an app instance
def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    api = Api(app)
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
    
    # register resources
    api.add_resource(UserRegistration, '/user/register')
    
    return app


