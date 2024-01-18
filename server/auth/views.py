# Handles the request

from flask_restful import Resource, reqparse, abort
from server.auth.models import UserModel, db

class UserRegistration(Resource):
    """User class view to register new objects"""
    
    parser = reqparse.RequestParser()
    parser.add_argument("name", 
                        required=True, 
                        help="Missing Name", 
                        type=str)
    parser.add_argument("description", 
                        required=True, 
                        help="Missing description", 
                        type=str)

    def post(self):
        args = self.parser.parse_args()
        name = args.get('name') #Bongani
        description = args.get('description')
        
        new_obj = UserModel(
            name=name, #Bongani
            description=description #"An active, responsive member"
        )
        
        try:
            db.session.add(new_obj)
            db.session.commit()    
        except Exception as e:
            db.session.rollback()
            abort(500, error=str(e))         
        finally:
            db.session.close()
            
        return {'message': 'User successfully created'}, 201
    
    def get(self):
        user = UserModel.query.all()
        
        if not user:
            abort(404, message="No user records found")
        
        user_data = [{
            "id": x.id,
            'name': x.name,
            "description": x.description
        } for x in user]
            
            
        return {"user": user_data}, 200
    
class UserList(Resource):
    """User class view to check a single record"""
    
    def get(self, id):
        pass
    
    def put(self, id):
        pass
    
    def delete(self, id):
        pass
