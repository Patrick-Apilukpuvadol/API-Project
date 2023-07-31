from flask import Flask, jsonify, request, Blueprint
from init import db
from models.tour_group_log import Tour_group_log
from models.customer_tour_booking import Customer_tour_booking, Customer_tour_bookingSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

customer_tour_bp = Blueprint('customer_tour', __name__)

@customer_tour_bp.route('/customer_tour_booking', methods=['GET'])
def get_customers():
    return jsonify(customer_id)

@customer_tour_bp.route('/customer_tour_booking/<int:tour_id>', methods=['GET'])
def get_tours(tour_id):
    tour = next((tour for tour in tour if tour['id'] == tour_id), None)
    if tour:
        return jsonify(tour_id)
    else:
        return jsonify({'error': 'Tour not found'}), 404

@customer_tour_bp.route('/customer_tour_booking', methods=['GET'])
def get_hotels():
    return jsonify(tour_id)

@customer_tour_bp.route('/customer_tour_booking/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = next((customer for customer in customer if customer['id'] == customer_id), None)
    if customer:
        return jsonify(customer_id)
    else:
        return jsonify({'error': 'Customer not found'}), 404

@customer_tour_bp.route('/customer_tour_booking', methods=['POST'])
def book_tour():
    data = request.get_json()
    customer_id = data['customer_id']
    tour_id = data['tour_id']
    tour = next((tour for tour in tour if tour['id'] == tour_id), None)
    if tour:
        return jsonify(tour_id)
    else:
        return jsonify({'error': 'Tour not found'}), 404