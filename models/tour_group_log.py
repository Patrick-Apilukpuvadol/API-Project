from init import db, ma
from marshmallow import Schema,fields
from marshmallow.validate import Length, And, Email


# defining the model for tour_group_log
class Tour_group_log(db.Model):
    __tablename__ = 'tour_group_log'
    
    tour_id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer, db.ForeignKey('customer_tour_booking.booking_id'), nullable=False)
    agent_id = db.Column(db.Integer, db.ForeignKey('agent.agent_id'), nullable=False)
    duration = db.Column(db.String)
    activities = db.Column(db.String)
    booking_fee = db.Column(db.Integer)
    

    
class Tour_group_logSchema(ma.Schema):
    customer_id = fields.Integer()
    agent_id = fields.Integer()
    tour_id = fields.Integer()
    duration = fields.String(required=True, validate=And(
        Length(min=2, error='Must be at least two characters long.')))
    activities = fields.String(required=True, validate=And(
        Length(min=2, error='Must be at least two characters long.')))
    booking_fee = fields.Integer(required=True, validate=And(
        Length(min=3, error='Price must be at least three integers long.')))
    booking_id = fields.Integer()
    
    class Meta:
        fields = ('customer_id', 'agent_id', 'tour_id', 'duration', 'activites', 'booking_fee', 'booking_id')
        ordered = True
        
        
tour_group_log_schema = Tour_group_logSchema()
tour_group_logs_schema = Tour_group_logSchema(many=True)