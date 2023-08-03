from init import db, ma
from marshmallow import Schema,fields
from marshmallow.validate import Length, And, Email

# defining the model for customer_tour_booking
class Customer_tour_booking(db.Model):
    __tablename__ = 'customer_tour_booking'
    
    tour_id = db.Column(db.Integer, db.ForeignKey('tour_group_log.tour_id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    contact_number = db.Column(db.String(50))
    contact_email = db.Column(db.String(50))
    

    
class Customer_tour_bookingSchema(ma,Schema):
    customer_id = fields.Integer()
    first_name = fields.String(required=True, validate=And(
        Length(min=2, error='The last name must be at least two characters long.')))
    last_name = fields.String(required=True, validate=And(
        Length(min=2, error='The last name must be at least two characters long.')))
    contact_number = fields.String(required=True, validate=And(
        Length(min=10, error='The mobile number must be 10 digits')))
    contact_email = fields.String(required=True, validate=Email)
    tour_id = fields.Integer()
    
    class Meta:
        fields = ('customer_id', 'first_name', 'last_name', 'contact_number', 'contact_email', 'tour_id')
        ordered = True
        
customer_tour_booking_schema = Customer_tour_bookingSchema()
customer_tour_bookings_schema = Customer_tour_bookingSchema(many=True)