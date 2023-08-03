from init import db, bcrypt
from flask import Blueprint, request
from models.agent import Agent, agent_schema
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from flask_jwt_extended import create_access_token
from datetime import timedelta

authentication_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

@authentication_blueprint.route('/register', methods=['POST']) # registering new user
def register():
    try:
        json_data = request.get_json() 
        agent=Agent()
        agent.first_name=json_data.get('first_name')
        agent.last_name=json_data.get('last_name')
        agent.contact_email=json_data.get('contact_email')
        if json_data.get('password'): 
            agent.password=bcrypt.generate_password_hash(json_data.get('password')).decode('utf-8')
        db.session.add(agent) 
        db.session.commit() 
        return agent_schema.dump(agent), 201 
    
    
    except IntegrityError as e: 
        if e.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return {'error': 'This email address is already in use.'}, 409
        if e.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {'error': f'The {e.orig.diag.column_name} is required.'}, 409
        
        
@authentication_blueprint.route('/login', methods=['POST']) # Route for logging in
def login():
    
    json_data = request.get_json() 
    stmt = db.select(Agent).filter_by(email=json_data.get('contact_email'))
    agent = db.session.scalar(stmt)
    
    if agent and bcrypt.check_password_hash(agent.password, json_data.get('password')):
        token = create_access_token(identity=str(agent.id), expires_delta=timedelta(days=7)) 
        return {'Login Succesful': Agent, 'email': agent.email, 'token': token, 'is_admin': agent.is_admin}
    else:
        return {'Error': 'You have entered the wrong email or the wrong password. Please try again.'}, 401 