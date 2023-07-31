from flask import Flask, jsonify, request, Blueprint
from init import db
from models.customer_tour_booking import Customer_tour_booking
from models.customer import Customer, CustomerSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

customer_bp = Blueprint('customer', __name__)

@customer_bp.route('/customer', methods=['GET'])
def get_customer():
    return jsonify(customer_id)

@customer_bp.route('/customer/<int:customer_id>', methods=['GET'])
def get_customer_id(customer_id):
    customer = next((customer for customer in customer if customer['id'] == customer), None)
    if customer:
        return jsonify(customer_id)
    else:
        return jsonify({'error': 'Tour not found'}), 404

@customer_bp.route('/agent', methods=['POST'])
def add_customer():
    data = request.get_json()
    customer_id = data['customer_id']
    customer = next((customer for customer in customer if customer['id'] == customer_id), None)
    if customer:
        return jsonify(customer_id)
    else:
        return jsonify({'error': 'Tour not found'}), 404