from flask import Flask, jsonify, request

@app.route('/agent', methods=['GET'])
def get_agents():
    return jsonify(agent_id)

@app.route('/agent/<int:agent_id>', methods=['GET'])
def get_agent_id(agent_id):
    agent = next((agent for agent in agent if agent['id'] == agent_id), None)
    if agent:
        return jsonify(agent_id)
    else:
        return jsonify({'error': 'Tour not found'}), 404

@app.route('/agent', methods=['POST'])
def add_agent_tour():
    data = request.get_json()
    agent_id = data['agent_id']
    agent = next((agent for agent in agent if agent['id'] == agent_id), None)
    if agent:
        return jsonify(agent_id)
    else:
        return jsonify({'error': 'Tour not found'}), 404