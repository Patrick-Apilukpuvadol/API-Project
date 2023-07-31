from flask import Flask, jsonify, request, Blueprint
from init import db
from models.tour_group_log import Tour_group_log
from models.agent import Agent, AgentSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

agent_bp = Blueprint('agent', __name__)

@agent_bp.route('/agent', methods=['GET'])
def get_agents():
    return jsonify(agent_id)

@agent_bp.route('/agent/<int:agent_id>', methods=['GET'])
def get_agent_id(agent_id):
    agent = next((agent for agent in agent if agent['id'] == agent_id), None)
    if agent:
        return jsonify(agent_id)
    else:
        return jsonify({'error': 'Tour not found'}), 404

@agent_bp.route('/agent', methods=['POST'])
def add_agent_tour():
    data = request.get_json()
    agent_id = data['agent_id']
    agent = next((agent for agent in agent if agent['id'] == agent_id), None)
    if agent:
        return jsonify(agent_id)
    else:
        return jsonify({'error': 'Tour not found'}), 404