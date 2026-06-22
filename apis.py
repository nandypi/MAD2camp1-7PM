from flask_restful import Resource, Api
from flask import request

from models import db, User, Item

api = Api()

# @app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
# def hello_world():
#     data = request.get_json()  # Get JSON data from the request body
#     if request.method == 'GET':
#         print("GET request received")
#     elif request.method == 'POST':
#         print("POST request received")
#     elif request.method == 'PUT':
#         print("PUT request received")
#     elif request.method == 'DELETE':
#         print("DELETE request received")
#     # return render_template('index.html') # this is what we were doing in mad1 project
#     return {"message": f"Hello, {data.get('name', 'World')}!"} # this is what we are doing in mad2 project

# TESTING API

class HelloWorld(Resource):
    def get(self):
        return {"message": "Get request received"}
    def post(self):
        data = request.get_json()  # Get JSON data from the request body
        print(data)
        return {"message": "Post request received", "data": data}
    def put(self):
        return {"message": "Put request received"}
    def delete(self):
        return {"message": "Delete request received"}
api.add_resource(HelloWorld, '/hello')

# ITEM API

class ItemAPI(Resource):
    def get(self, item_id=None):
        if item_id is not None:
            item = Item.query.get(item_id)
            if not item:
                return {"message": f"Item not found with ID {item_id}"}, 404
            return {"message": f"Item with ID {item_id} retrieved successfully", "data": item.to_dict()}
        items = [item.to_dict() for item in Item.query.all()]
        return {"message": "All items retrieved successfully", "data": items}
    def post(self, item_id=None):
        if item_id:
            return {"message": "Item id is not required for creating an item"}, 400
        data = request.get_json()  # Get JSON data from the request body
        if not data or not data.get('name'):
            return {"message": "Please provide all required fields"}, 400
        item = Item(name=data['name'], description=data.get('description'), image_url=data.get('image_url'))
        db.session.add(item)
        db.session.commit()
        return {"message": "Successfully created item", "data": data}
    def put(self, item_id=None):
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
        return {"message": f"Successfully updated item with ID {item_id}", "data": data}
    def delete(self, item_id=None):
        if not item_id:
            return {"message": "Item ID is required for deleting an item"}, 400
        item = Item.query.get(item_id)
        if not item:
            return {"message": f"Item not found with ID {item_id}"}, 404
        db.session.delete(item)
        db.session.commit()
        return {"message": f"Successfully deleted item with ID {item_id}"}
api.add_resource(ItemAPI, '/items', '/items/<int:item_id>')

