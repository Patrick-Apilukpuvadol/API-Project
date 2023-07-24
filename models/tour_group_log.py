from init import db, ma
from marshmallow import fields

class Tour_group_log(db.Model):
    __tablename__ = 'tour_group_log'
    
    tour_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)
    agent_id = db.Column(db.Integer, db.ForeignKey('agent.agent_id'), nullable=False)
    duration = db.Column(db.String(50))
    activities = db.Column(db.String(50))
    booking_fee = db.Column(db.Integer)
    
class Tour_group_logSchema(ma,Schema):
    