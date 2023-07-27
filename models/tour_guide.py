from init import db, ma
from marshmallow import Schema,fields

class Tour_guide(db.Model):
    __tablename__ = 'tour_guide'
    
    guide_id = db.Column(db.Integer, primary_key=True)
    tour_id = db.Column(db.Integer, db.ForeignKey('tour_group_log.tour_id'), nullable=False)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    company_name = db.Column(db.String(50))
    emergency_contact = db.Column(db.String(50))
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod
    def get_by_id(cls,id):
        return cls.query.get_or_404(id)
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
class Tour_guideSchema(ma,Schema):
    guide_id = fields.Integer()
    tour_id = fields.Integer()
    first_name = fields.String(50)
    last_name = fields.String(50)
    company_name = fields.String(50)
    emergency_contact = fields.String(50)
    
    