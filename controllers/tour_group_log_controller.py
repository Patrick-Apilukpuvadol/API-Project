from flask import Flask, jsonify, request

@app.route('/tour_group_log', methods=['GET'])
def get_log():
    return jsonify(tour_id)

@app.route('/customer_tour_booking/<int:tour_id>', methods=['GET'])
def get_tours(tour_id):
    tour = next((tour for tour in tour if tour['id'] == tour_id), None)
    if tour:
        return jsonify(tour_id)
    else:
        return jsonify({'error': 'Tour not found'}), 404

@app.route('/customer_tour_booking', methods=['GET'])
def get_hotels():
    return jsonify(tour_id)

@app.route('/customer_tour_booking/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = next((customer for customer in customer if customer['id'] == customer_id), None)
    if customer:
        return jsonify(customer_id)
    else:
        return jsonify({'error': 'Customer not found'}), 404

@app.route('/customer_tour_booking', methods=['POST'])
def book_tour():
    data = request.get_json()
    customer_id = data['customer_id']
    tour_id = data['tour_id']
    tour = next((tour for tour in tour if tour['id'] == tour_id), None)
    if tour:
        return jsonify(tour_id)
    else:
        return jsonify({'error': 'Tour not found'}), 404