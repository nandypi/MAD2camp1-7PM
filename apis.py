from flask_restful import Resource, Api
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token

from models import db, User, Item

api = Api()

# TESTING API

class HelloWorld(Resource):
    def get(self):
        return {"message": "Hello, greetings from the backend!"}
    def post(self):
        data = request.get_json()  # Get JSON data from the request body
        print(data)
        return {"message": "Post request received", "data": data}
    def put(self):
        return {"message": "Put request received"}
    def delete(self):
        return {"message": "Delete request received"}
api.add_resource(HelloWorld, '/hello')

# Auth Endpoints

class Login(Resource):
    def post(self):
        data = request.get_json()
        if not data or not data.get('email') or not data.get('password'):
            return {"message": "Please provide both email and password"}, 400
        user = User.query.filter_by(email=data['email']).first()
        if not user or user.password != data['password']:
            return {"message": "Invalid email or password"}, 401
        access_token = create_access_token(identity=user.email)
        return {"message": "Login successful", "access_token": access_token, "user": user.to_dict()}
api.add_resource(Login, '/login')

class Register(Resource):
    def post(self):
        data = request.get_json()
        if not data or not data.get('email') or not data.get('password'):
            return {"message": "Please provide both email and password"}, 400
        if User.query.filter_by(email=data['email']).first():
            return {"message": "Email already exists"}, 400
        user = User(email=data['email'], password=data['password'])
        db.session.add(user)
        db.session.commit()
        return {"message": "User registered successfully", "user": user.to_dict()}
api.add_resource(Register, '/register')

def IsAdmin():
    user = User.query.filter_by(email=get_jwt_identity()).first()
    return user.role == 'admin'

# ITEM API

class ItemAPI(Resource):

    @jwt_required()
    def get(self, item_id=None):
        if item_id is not None:
            item = Item.query.get(item_id)
            if not item:
                return {"message": f"Item not found with ID {item_id}"}, 404
            return {"message": f"Item with ID {item_id} retrieved successfully", "item": item.to_dict()}
        items = [item.to_dict() for item in Item.query.all()]
        return {"message": "All items retrieved successfully", "items": items}
    
    @jwt_required()
    def post(self, item_id=None):
        if not IsAdmin():
            return {"message": "Admin privileges required to create an item"}, 403

        if item_id:
            return {"message": "Item id is not required for creating an item"}, 400
        data = request.get_json()  # Get JSON data from the request body
        if not data or not data.get('name'):
            return {"message": "Please provide all required fields"}, 400
        item = Item(name=data['name'], description=data.get('description'), image_url=data.get('image_url'))
        db.session.add(item)
        db.session.commit()
        return {"message": "Successfully created item", "item": data}
    
    @jwt_required()
    def put(self, item_id=None):
        if not IsAdmin():
            return {"message": "Admin privileges required to create an item"}, 403

        if not item_id:
            return {"message": "Item ID is required for updating an item"}, 400
        data = request.get_json()
        if not data or not all(key in data for key in ['name', 'description', 'image_url']):
            return {"message": "Please provide required data for updating the item"}, 400
        item = Item.query.get(item_id)
        if not item:
            return {"message": f"Item not found with ID {item_id}"}, 404
        for key, value in data.items():
            if hasattr(item, key):
                setattr(item, key, value)
        db.session.commit()
        return {"message": f"Successfully updated item with ID {item_id}", "item": data}
    
    @jwt_required()
    def delete(self, item_id=None):
        if not IsAdmin():
            return {"message": "Admin privileges required to delete an item"}, 403

        if not item_id:
            return {"message": "Item ID is required for deleting an item"}, 400
        item = Item.query.get(item_id)
        if not item:
            return {"message": f"Item not found with ID {item_id}"}, 404
        db.session.delete(item)
        db.session.commit()
        return {"message": f"Successfully deleted item with ID {item_id}"}
    
api.add_resource(ItemAPI, '/items', '/items/<int:item_id>')

