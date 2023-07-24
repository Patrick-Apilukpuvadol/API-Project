from init import db, ma
from marshmallow import fields

class Tour_guide(db.Model):
    __tablename__ = 'tour_guide'
    
    guide_id = db.Column(db.Integer, primary_key=True)
    tour_id = db.Column(db.Integer, db.ForeignKey('tour_group_log.tour_id'), nullable=False)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    company_name = db.Column(db.String(50))
    emergency_contact = db.Column(db.String(50))
    
class Tour_guideSchema(ma,Schema):
    
    
    