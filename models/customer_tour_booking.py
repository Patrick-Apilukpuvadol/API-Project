from init import db, ma
from marshmallow import Schema,fields

class Customer_tour_booking(db.Model):
    __tablename__ = 'customer_tour_booking'
    
    tour_id = db.Column(db.Integer, db.ForeignKey('tour_group_log.tour_id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    contact_number = db.Column(db.String(50))
    contact_email = db.Column(db.String(50))
    
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
    
class Customer_tour_bookingSchema(ma,Schema):
    customer_id = fields.Integer()
    first_name = fields.String(50)
    last_name = fields.String(50)
    contact_number = fields.String(50)
    contact_email = fields.String(50)
    tour_id = fields.Integer()