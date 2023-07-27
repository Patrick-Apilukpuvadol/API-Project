from init import db, ma
from marshmallow import Schema,fields

class Tour_group_log(db.Model):
    __tablename__ = 'tour_group_log'
    
    tour_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)
    agent_id = db.Column(db.Integer, db.ForeignKey('agent.agent_id'), nullable=False)
    duration = db.Column(db.String(50))
    activities = db.Column(db.String(50))
    booking_fee = db.Column(db.Integer)
    
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
    
class Tour_group_logSchema(ma,Schema):
    customer_id = fields.Integer()
    agent_id = fields.Integer()
    tour_id = fields.Integer()
    duration = fields.String(50)
    activities = fields.String(50)
    booking_fee = fields.Integer()