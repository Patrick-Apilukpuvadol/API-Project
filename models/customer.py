from init import db, ma
from marshmallow import fields

class Customer(db.Model):
    __tablename__ = 'customer'
    
    customer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    contact_number = db.Column(db.String(50))
    contact_email = db.Column(db.String(50))
    emergency_contact = db.Column(db.String(50))
    
    customers = db.relationship('')
    
class CustomerSchema(ma,Schema):
    