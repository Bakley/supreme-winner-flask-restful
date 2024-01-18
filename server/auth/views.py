from flask_restful import Resource, reqparse, abort
from server.auth.models import UserModel, db

class UserRegistration(Resource):
    """User class view to register new objects"""

    parser = reqparse.RequestParser()
    parser.add_argument("name", required=True, help="Name is required", type=str)
    parser.add_argument("description", required=True, help="Description is required", type=str)


    def _validate_uniqueness(self, name):
        """Validate uniqueness of user name"""
        if UserModel.query.filter_by(name=name).first():
            abort(400, 
                message=f"A user with the name '{name}' already exists. Please choose a different name."
            )

    def post(self):
        args = self.parser.parse_args()
        name, description = args.get('name'), args.get('description')
                
        # Validate uniqueness
        self._validate_uniqueness(name)
        
        new_obj = UserModel(name=name, description=description)
        
        try:
            db.session.add(new_obj)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            abort(500, error=f"Error creating user: {str(e)}")
        finally:
            db.session.close()
            
        return {
            'message': f"User '{name}' successfully created with description: '{description}'"
            }, 201
    
    def get(self):
        users = UserModel.query.all()
        
        if not users:
            abort(404, message="No user records found")
        
        user_data = [{
            "id": user.id,
            'name': user.name,
            "description": user.description
        } for user in users]
            
        return {
            "message": "User records retrieved successfully",
            "users": user_data
            }, 200
