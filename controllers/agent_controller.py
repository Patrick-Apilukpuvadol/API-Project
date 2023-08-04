from flask import Flask, jsonify, request, Blueprint
from init import db
from models.tour_group_log import Tour_group_log
from models.agent import Agent, AgentSchema, agent_schema, agents_schema
from flask_jwt_extended import jwt_required, get_jwt_identity

agent_bp = Blueprint('agent', __name__)

def admin_authorised():
    agent_id = get_jwt_identity()
    stmt = db.select(Agent).filter_by(id=agent_id)
    agent = db.session.scalar(stmt)
    return agent.is_admin

@agent_bp.route('/', methods=['GET'])
def get_agents():
    stmt = db.select(Agent).order_by(Agent.id.desc())
    agent = db.session.scalars(stmt)
    return agents_schema.dump(agent)

@agent_bp.route('/<int:agent_id>', methods=['GET'])
def get_agent_id(agent_id):
    stmt = db.select(Agent).filter_by(id=id)
    agent = db.session.scalar(stmt)
    if agent:
        return agent_schema.dump([agent])
    else:
        return {'error': f'Agent with the id {id} does not exist.'}

@agent_bp.route('/', methods=['POST'])
@jwt_required
def add_agent():
    json_data = agent_schema.load(request.get_json())
    agent = Agent( # creating the new agent
        agent_id=get_jwt_identity(),
        first_name=json_data.get('first_name'),
        last_name=json_data.get('last_name'),
        contact_number=json_data.get('contact_number'),
        contact_email=json_data.get('contact_email'),
        emergency_contact=json_data.get('emergency_contact'),
        password=json_data.get('password')
    )
    db.session.add(agent) # Creates new Agent for session
    db.session.commit() # Commits creation of new agent
    return agent_schema.dump(agent), 201 # Returns result to user

