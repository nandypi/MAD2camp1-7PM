from flask import Flask, request
from flask_jwt_extended import JWTManager
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Change this to a random secret key
jwt = JWTManager(app)

# connect to database
from models import db, User
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

# connect to api
from apis import api
api.init_app(app)


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



if __name__ == '__main__':

    with app.app_context():
        db.create_all()

        admin = User.query.filter_by(role='admin').first()
        if not admin:
            print("No admin user found.\nCreating default admin user with email: admin@gmail.com and password: password")
            admin = User(email="admin@gmail.com", password="password", role="admin")
            db.session.add(admin)
            db.session.commit()
        else:
            print("Admin already exists with email: admin@gmail.com and password: password")

    app.run(debug=True)