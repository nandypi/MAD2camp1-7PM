from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello_world():
    data = request.get_json()  # Get JSON data from the request body
    if request.method == 'GET':
        print("GET request received")
    elif request.method == 'POST':
        print("POST request received")
    elif request.method == 'PUT':
        print("PUT request received")
    elif request.method == 'DELETE':
        print("DELETE request received")
    # return render_template('index.html') # this is what we were doing in mad1 project
    return {"message": f"Hello, {data.get('name', 'World')}!"} # this is what we are doing in mad2 project

api = Api(app)

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

if __name__ == '__main__':
    app.run(debug=True)