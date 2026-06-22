from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(50), nullable=False, default='user')

    def __repr__(self):
        return f'<User {self.email} | Role: {self.role}>'
    
    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "role": self.role
        }
    
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    image_url = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f'<Item {self.name}>'
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "image_url": self.image_url
        }
    
