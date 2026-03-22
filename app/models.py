from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class Property(db.Model):
    __tablename__ = 'properties'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    no_of_bedrooms = db.Column(db.Integer, nullable=False)
    no_of_bathrooms = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    image_filename = db.Column(db.String(255), nullable=True)

    def __init__(self, title, type, no_of_bedrooms, no_of_bathrooms, description, price, location, image_filename):
        self.title = title
        self.type = type
        self.no_of_bedrooms = no_of_bedrooms
        self.no_of_bathrooms = no_of_bathrooms
        self.description = description
        self.price = price
        self.location = location
        self.image_filename = image_filename
    
