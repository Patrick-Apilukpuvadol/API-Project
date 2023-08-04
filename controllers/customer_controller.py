from flask import Flask, jsonify, request, Blueprint
from init import db
from models.customer_tour_booking import Customer_tour_booking
from models.customer import Customer, CustomerSchema, customer_schema, customers_schema
from controllers.agent_controller import admin_authorised
from flask_jwt_extended import jwt_required, get_jwt_identity

customer_bp = Blueprint('customer', __name__)

@customer_bp.route('/', methods=['GET'])
def get_customer():
    stmt = db.select(Customer).order_by(Customer.customer_id.desc())
    customers = db.session.scalars(stmt)
    return customers_schema.dump(customers)

@customer_bp.route('/<int:customer_id>', methods=['GET'])
def get_customer_id(customer_id):
    stmt = db.select(Customer).filter_by(customer_id=customer_id)
    customer = db.session.scalar(stmt) 
    if customer:
        return customer_schema.dump(customer) # displays result of query
    else:
        return {'error': f'Customer with the id {id} does not exist.'}, 404 #display error if unsuccessful

@customer_bp.route('/', methods=['POST'])
@jwt_required()
def add_customer():
    json_data = customer_schema.load(request.get_json())
    customer = Customer( # creating the new customer
        customer_id=get_jwt_identity(),
        first_name=json_data.get('first_name'),
        last_name=json_data.get('last_name'),
        contact_number=json_data.get('contact_number'),
        contact_email=json_data.get('contact_email'),
        emergency_contact=json_data.get('emergency_contact'),
        
    )
    db.session.add(customer) # Creates new customer for session
    db.session.commit() # Commits creation of new customer
    return customer_schema.dump(customer), 201

@customer_bp.route('/<int:customer_id>', methods=['DELETE'])
@jwt_required()
def delete_customer(customer_id): #deletes the customer 
    
    admin_status = admin_authorised() # authorise_admin function
    if not admin_status:
        return {'error': 'You do not possess Admin rights to delete this customer'} # if not admin will return error message
    stmt = db.select(Customer).filter_by(customer_id=customer_id) # queries and searches for id
    customer = db.session.scalar(stmt)
    if customer:
        db.session.delete(customer)
        db.session.commit()
        return {'message': f'Customer {customer.first_name} has been deleted succesfully.'} # Confirmation if query was successful and request has been carried out
    else:
        return {'error': f'Customer with the id {id} does not exist.'}, 404 
    
@customer_bp.route('/<int:customer_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_customer(id): #will query and select customer if found and update 
    
    json_data = customer_schema.load(request.get_json(), partial=True) 
    stmt = db.select(Customer).filter_by(customer_id=customer_id)
    customer = db.session.scalar(stmt)
    if customer:
        if str(customer.customer_id) != get_jwt_identity():
            return {'error': 'You must possess Admin Rights to update this customer.'}, 403 
        customer_id=get_jwt_identity(),
        first_name=json_data.get('first_name'),
        last_name=json_data.get('last_name'),
        contact_number=json_data.get('contact_number'),
        contact_email=json_data.get('contact_email'),
        emergency_contact=json_data.get('emergency_contact')
        return customer_schema.dump(customer) # If found will select and update information
    else:
        return {'error': f'Error Customer with id {id} does not exist.'}, 404