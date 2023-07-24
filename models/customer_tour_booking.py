from init import db, ma
from marshmallow import fields

class Customer_tour_booking(db.Model):
    __tablename__ = 'customer_tour_booking'
    
    tour_id = db.Column(db.Integer, db.ForeignKey('tour_group_log.tour_id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)
    agent_id = db.Column(db.Integer, db.ForeignKey('agent.agent_id'), nullable=False)
    duration = db.Column(db.String(50))
    activities = db.Column(db.String(50))
    booking_fee = db.Column(db.Integer)