from flask import Flask, jsonify, request

@app.route('/tour_guide', methods=['GET'])
def get_tour_guide():
    return jsonify(guide_id)

@app.route('/tour_guide/<int:guide_id>', methods=['GET'])
def get_guide_id(guide_id):
    guide = next((guide for guide in guide if guide['id'] == guide_id), None)
    if guide:
        return jsonify(guide_id)
    else:
        return jsonify({'error': 'Tour not found'}), 404

@app.route('/tour_guide', methods=['POST'])
def add_guide_id():
    data = request.get_json()
    guide_id = data['guide_id']
    guide = next((guide for guide in guide if guide['id'] == guide_id), None)
    if guide:
        return jsonify(guide_id)
    else:
        return jsonify({'error': 'Guide not found'}), 404