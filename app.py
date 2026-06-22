from flask import Flask, request


app = Flask(__name__)

# connect to database
from models import db, User
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

# connect to api
from apis import api
api.init_app(app)


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