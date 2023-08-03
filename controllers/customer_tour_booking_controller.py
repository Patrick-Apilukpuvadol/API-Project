from flask import Flask, jsonify, request, Blueprint
from init import db
from models.tour_group_log import Tour_group_log
from models.customer_tour_booking import Customer_tour_booking, Customer_tour_bookingSchema, customer_tour_booking_schema, customer_tour_bookings_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from agent_controller import admin_authorised

customer_tour_bp = Blueprint('customer_tour', __name__)

@customer_tour_bp.route('/customer_tour_booking', methods=['GET'])
def get_customers():
    return jsonify(customer_id)

@customer_tour_bp.route('/', methods=['GET'])
def get_customer_log():
    stmt = db.select(Customer_tour_booking).order_by(Customer_tour_booking.customer_id.desc())
    customer_log = db.session.scalars(stmt)
    return customer_tour_bookings_schema.dump(customer_log)

@customer_tour_bp.route('<int:customer_id>', methods=['GET'])
def get_customer_log_id(customer_id):
    stmt = db.select(Customer_tour_booking).filter_by(customer_id=customer_id)
    customer_log = db.session.scalar(stmt) 
    if customer_log:
        return customer_tour_bookings_schema.dump(customer_log) # displays result of query
    else:
        return {'error': f'Error Tour with id {id} does not exist.'}, 404 #display error if unsuccessful

@customer_tour_bp.route('/', methods=['POST'])
@jwt_required()
def add_customer_log():
    json_data = customer_tour_bookings_schema.load(request.get_json())
    customer_log = Customer_tour_booking( # creating the new customer log
        customer_id=get_jwt_identity(),
        first_name=json_data.get('first_name'),
        last_name=json_data.get('last_name'),
        contact_number=json_data.get('contact_number'),
        contact_email=json_data.get('contact_email'),
        tour_id=json_data.get('tour_id'),
        
    )
    db.session.add(customer_log) # Creates new customer log for session
    db.session.commit() # Commits creation of new customer log
    return customer_tour_booking_schema.dump(customer_log), 201 # Returns result to user

@customer_tour_bp.route('/<int:customer_id>', methods=['DELETE'])
@jwt_required()
def delete_customer_log(customer_id): #deletes the customer log while making user user has admin rights
    
    admin_status = admin_authorised() # authorise_admin function checks whether user has admin permissions
    if not admin_status:
        return {'error': 'You do not possess Admin rights to delete this customer log'} # if not admin return this error message
    stmt = db.select(Customer_tour_booking).filter_by(customer_id=customer_id) # queries and searches for specific id
    customer_log = db.session.scalar(stmt)
    if customer_log:
        db.session.delete(customer_log)
        db.session.commit()
        return {'message': f'Customer Log {customer_log.customer_id} has been deleted succesfully.'} # Confirmation if query was successful and request has been carried out
    else:
        return {'error': f'Error Customer log with the id {id} does not exist.'}, 404 
    
@customer_tour_bp.route('/<int:customer_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_customer_log(customer_id): #will query and select customer log if found and update 
    
    json_data = customer_tour_booking_schema.load(request.get_json(), partial=True) 
    stmt = db.select(Tour_group_log).filter_by(customer_id=customer_id) 
    customer_log = db.session.scalar(stmt)
    if customer_log:
        if str(customer_log.customer_id) != get_jwt_identity():
            return {'error': 'You must possess Admin Rights to update this Tour log.'}, 403 
        tour_id=get_jwt_identity(),
        customer_id=json_data.get('customer_id'),
        agent_id=json_data.get('agent_id'),
        duration=json_data.get('duration'),
        activities=json_data.get('activities'),
        booking_fee=json_data.get('booking_fee'),
        return customer_tour_booking_schema.dump(customer_log) # If found will select and update information
    else:
        return {'error': f'Error Customer log with id {id} does not exist.'}, 404