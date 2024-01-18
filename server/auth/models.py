# Connection to the database, we are using an ORM

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(140), nullable=False)

    
    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description
