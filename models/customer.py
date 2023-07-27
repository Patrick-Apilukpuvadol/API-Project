from init import db, ma
from marshmallow import Schema,fields

class Customer(db.Model):
    __tablename__ = 'customer'
    
    customer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    contact_number = db.Column(db.String(50))
    contact_email = db.Column(db.String(50))
    emergency_contact = db.Column(db.String(50))
    
    customers = db.relationship('')
    
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
    
class CustomerSchema(ma,Schema):
    customer_id = fields.Integer()
    first_name = fields.String(50)
    last_name = fields.String(50)
    contact_number = fields.String(50)
    contact_email = fields.String(50)
    emergency_contact = fields.String(50)