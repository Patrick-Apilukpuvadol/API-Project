from init import db, ma
from marshmallow import Schema,fields
from marshmallow.validate import Length, And, Email


# defining the model for tour_guide
class Tour_guide(db.Model):
    __tablename__ = 'tour_guide'
    
    guide_id = db.Column(db.Integer, primary_key=True)
    tour_id = db.Column(db.Integer, db.ForeignKey('tour_group_log.tour_id'), nullable=False)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    company_name = db.Column(db.String)
    emergency_contact = db.Column(db.String)
    
    
class Tour_guideSchema(ma.Schema):
    guide_id = fields.Integer()
    tour_id = db.Column(db.Integer, db.ForeignKey('tour_group_log.tour_id'), nullable=False)
    first_name = fields.String(required=True, validate=And(
        Length(min=2, error='The first name must be at least two characters long.')))
    last_name = fields.String(required=True, validate=And(
        Length(min=2, error='The last name must be at least two characters long.')))
    company_name = fields.String(required=True, validate=And(
        Length(min=2, error='The name of company must be at least two characters long.')))
    emergency_contact = fields.String(required=True, validate=And(
        Length(min=9, error='The mobile number must be 10 digits')))
    
    class Meta:
        fields = ('guide_id', 'tour_id', 'first_name', 'last_name', 'company_name', 'emergency_contact')
        ordered = True
    
    
tour_guide_schema = Tour_guideSchema()
tour_guides_schema = Tour_guideSchema(many=True)