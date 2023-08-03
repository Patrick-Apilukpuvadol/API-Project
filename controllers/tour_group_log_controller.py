from flask import Flask, jsonify, request, Blueprint
from init import db
from agent_controller import admin_authorised
from models.tour_group_log import Tour_group_log,Tour_group_logSchema, tour_group_log_schema, tour_group_logs_schema
from flask_jwt_extended import jwt_required, get_jwt_identity

tour_group_bp = Blueprint('tour_group_log', __name__)

@tour_group_bp.route('/', methods=['GET'])
def get_tour_log():
    stmt = db.select(Tour_group_log).order_by(Tour_group_log.tour_id_id.desc())
    tour_log = db.session.scalars(stmt)
    return tour_group_logs_schema.dump(tour_log)

@tour_group_bp.route('<int:tour_id>', methods=['GET'])
def get_tour_log_id(tour_id):
    stmt = db.select(Tour_group_log).filter_by(tour_id=tour_id)
    tour_log = db.session.scalar(stmt) 
    if tour_log:
        return tour_group_log_schema.dump(tour_log) # displays result of query
    else:
        return {'error': f'Error Tour with id {id} does not exist.'}, 404 #display error if unsuccessful

@tour_group_bp.route('/', methods=['POST'])
@jwt_required()
def add_tour_log():
    json_data = tour_group_log_schema.load(request.get_json())
    tour_log = Tour_group_log( # creating the new tour log
        tour_id=get_jwt_identity(),
        customer_id=json_data.get('customer_id'),
        agent_id=json_data.get('agent_id'),
        duration=json_data.get('duration'),
        activities=json_data.get('activities'),
        booking_fee=json_data.get('booking_fee'),
        
    )
    db.session.add(tour_log) # Creates new tour log for session
    db.session.commit() # Commits creation of new tour log
    return tour_group_log_schema.dump(tour_log), 201 # Returns result to user

@tour_group_bp.route('/<int:tour_id>', methods=['DELETE'])
@jwt_required()
def delete_tour_log(tour_id): #deletes the tour log while making user user has admin rights
    
    admin_status = admin_authorised() # authorise_admin function checks whether user has admin permissions
    if not admin_status:
        return {'error': 'You do not possess Admin rights to delete this customer'} # if not admin return this error message
    stmt = db.select(Tour_group_log).filter_by(tour_id=tour_id) # queries and searches for specific id
    tour_log = db.session.scalar(stmt)
    if tour_log:
        db.session.delete(tour_log)
        db.session.commit()
        return {'message': f'Tour Log {tour_log.tour_id} has been deleted succesfully.'} # Confirmation if query was successful and request has been carried out
    else:
        return {'error': f'Error Tour log with the id {id} does not exist.'}, 404 
    
@tour_group_bp.route('/<int:tour_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_tour_log(tour_id): #will query and select tour log if found and update 
    
    json_data = tour_group_log_schema.load(request.get_json(), partial=True) 
    stmt = db.select(Tour_group_log).filter_by(tour_id=tour_id) 
    tour_log = db.session.scalar(stmt)
    if tour_log:
        if str(tour_log.tour_id) != get_jwt_identity():
            return {'error': 'You must possess Admin Rights to update this Tour log.'}, 403 
        tour_id=get_jwt_identity(),
        customer_id=json_data.get('customer_id'),
        agent_id=json_data.get('agent_id'),
        duration=json_data.get('duration'),
        activities=json_data.get('activities'),
        booking_fee=json_data.get('booking_fee'),
        return tour_group_log_schema.dump(tour_log) # If found will select and update information
    else:
        return {'error': f'Error Tour log with id {id} does not exist.'}, 404