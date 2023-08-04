from init import db, ma
from marshmallow import Schema,fields
from marshmallow.validate import Length, And, Email

# defining the model for customer
class Customer(db.Model):
    __tablename__ = 'customer'
    
    customer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    contact_number = db.Column(db.String)
    contact_email = db.Column(db.String, nullable=False, unique=True)
    emergency_contact = db.Column(db.String)
    
    
    

    
class CustomerSchema(ma.Schema):
    customer_id = fields.Integer()
    first_name = fields.String(required=True, validate=And(
        Length(min=2, error='The first name must be at least two characters long.')))
    last_name = fields.String(required=True, validate=And(
        Length(min=2, error='The last name must be at least two characters long.')))
    contact_number = fields.String(required=True, validate=And(
        Length(min=10, error='The mobile number must be 10 digits')))
    contact_email = fields.String(required=True, validate=Email)
    emergency_contact = fields.String(required=True, validate=And(
        Length(min=10, error='The mobile number must be 10 digits')))
    
    class Meta:
        fields = ('customer_id', 'first_name', 'last_name', 'contact_number', 'contact_email', 'emergency_contact', 'is_admin')
        ordered = True
        
customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)