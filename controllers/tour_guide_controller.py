from flask import Flask, jsonify, request, Blueprint
from init import db
from models.tour_group_log import Tour_group_log
from models.tour_guide import Tour_guide, Tour_guideSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

tour_guide_bp = Blueprint('tour_guide', __name__)

@tour_guide_bp.route('/tour_guide', methods=['GET'])
def get_tour_guide():
    return jsonify(guide_id)

@tour_guide_bp.route('/tour_guide/<int:guide_id>', methods=['GET'])
def get_guide_id(guide_id):
    guide = next((guide for guide in guide if guide['id'] == guide_id), None)
    if guide:
        return jsonify(guide_id)
    else:
        return jsonify({'error': 'Tour not found'}), 404

@tour_guide_bp.route('/tour_guide', methods=['POST'])
def add_guide_id():
    data = request.get_json()
    guide_id = data['guide_id']
    guide = next((guide for guide in guide if guide['id'] == guide_id), None)
    if guide:
        return jsonify(guide_id)
    else:
        return jsonify({'error': 'Guide not found'}), 404