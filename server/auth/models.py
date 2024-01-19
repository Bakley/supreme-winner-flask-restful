# Connection to the database, we are using an ORM

import jwt
import os

from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

db = SQLAlchemy()

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(140), nullable=False)
    
    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description
        
    def generate_token(self, name, id):
        
        try:
            object_data = {
                "initail_time" : datetime.utcnow,
                "end_time": datetime.utcnow + timedelta(minutes=60),
                "user_name" : name,
                "user_id": id
            }
            
            token = jwt.encode(
                object_data, 
                str(current_app.os.getenv('SECRET_KEY')), 
                algorithm='HS256'
            )
            
            return token
        except Exception as e:
            return str(e)

    def decode_token(self, token):
        
        token_data = jwt.decode(token,
                                str(current_app.os.getenv('SECRET_KEY')),
                                algorithms='HS256')
        
        return token_data
