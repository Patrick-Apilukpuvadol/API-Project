from init import db, ma
from marshmallow import fields

class Customer_tour_booking(db.Model):
    __tablename__ = 'customer_tour_booking'
    
    agent_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    contact_number = db.Column(db.String(50))
    contact_email = db.Column(db.String(50))
    emergency_contact = db.Column(db.String(50))