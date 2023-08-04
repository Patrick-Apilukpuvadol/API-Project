from flask import Flask, jsonify, request, Blueprint
from controllers.agent_controller import admin_authorised
from init import db
from models.tour_group_log import Tour_group_log
from models.tour_guide import Tour_guide, Tour_guideSchema, tour_guide_schema, tour_guides_schema
from flask_jwt_extended import jwt_required, get_jwt_identity

tour_guide_bp = Blueprint('tour_guide', __name__)



@tour_guide_bp.route('/', methods=['GET'])
def get_tour_guides():
    stmt = db.select(Tour_guide).order_by(Tour_guide.guide_id.desc())
    tour_guide = db.session.scalars(stmt)
    return tour_guides_schema.dump(tour_guide)

@tour_guide_bp.route('/<int:guide_id>', methods=['GET'])
def get_tour_guide_id(guide_id):
    stmt = db.select(Tour_guide).filter_by(guide_id=guide_id)
    tour_guide = db.session.scalar(stmt) 
    if tour_guide:
        return tour_guides_schema.dump(tour_guide) # displays result of query
    else:
        return {'error': f'Tour guide with the id {id} does not exist.'}, 404 #display error if unsuccessful

@tour_guide_bp.route('/', methods=['POST'])
@jwt_required()
def add_tour_guide():
    json_data = tour_guides_schema.load(request.get_json())
    tour_guide = Tour_guide( # creating the new tour guide
        guide_id=get_jwt_identity(),
        tour_id=json_data.get('tour_id'),
        first_name=json_data.get('first_name'),
        last_name=json_data.get('last_name'),
        company_name=json_data.get('company_name'),
        emergency_contact=json_data.get('emergency_contact'),
        
    )
    db.session.add(tour_guide) # Creates new tour guide for session
    db.session.commit() # Commits creation of new tour guide
    return tour_guides_schema.dump(tour_guide), 201 # Returns result to user

@tour_guide_bp.route('/<int:guide_id>', methods=['DELETE'])
@jwt_required()
def delete_tour_guide(guide_id): #deletes the tour guide 
    
    admin_status = admin_authorised() # authorise_admin function 
    if not admin_status:
        return {'error': 'You do not possess Admin rights to delete this customer'} # if not admin will return error message
    stmt = db.select(Tour_guide).filter_by(guide_id=guide_id) # queries and searches for id
    tour_guide = db.session.scalar(stmt)
    if tour_guide:
        db.session.delete(tour_guide)
        db.session.commit()
        return {'message': f'Tour Guide {tour_guide.first_name} has been deleted succesfully.'} # Confirmation if query was successful and request has been carried out
    else:
        return {'error': f'Error Tour Guide with the id {id} does not exist.'}, 404 
    
@tour_guide_bp.route('/<int:guide_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_tour_guide(guide_id): #will query and select tour guide if found and update 
    
    json_data = tour_guides_schema.load(request.get_json(), partial=True) 
    stmt = db.select(Tour_guide).filter_by(guide_id=guide_id) 
    tour_guide = db.session.scalar(stmt)
    if tour_guide:
        if str(tour_guide.guide_id) != get_jwt_identity():
            return {'error': 'You must possess Admin Rights to update this customer.'}, 403 
        guide_id=get_jwt_identity(),
        tour_id=json_data.get('tour_id'),
        first_name=json_data.get('first_name'),
        last_name=json_data.get('last_name'),
        company_name=json_data.get('company_name'),
        emergency_contact=json_data.get('emergency_contact'),
        return tour_guides_schema.dump(tour_guide) # If found will select and update information
    else:
        return {'error': f'Error Tour Guide with id {id} does not exist.'}, 404