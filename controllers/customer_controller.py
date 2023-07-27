from flask import Flask, jsonify, request

@app.route('/customer', methods=['GET'])
def get_customer():
    return jsonify(customer_id)

@app.route('/customer/<int:customer_id>', methods=['GET'])
def get_customer_id(customer_id):
    customer = next((customer for customer in customer if customer['id'] == customer), None)
    if customer:
        return jsonify(customer_id)
    else:
        return jsonify({'error': 'Tour not found'}), 404

@app.route('/agent', methods=['POST'])
def add_customer():
    data = request.get_json()
    customer_id = data['customer_id']
    customer = next((customer for customer in customer if customer['id'] == customer_id), None)
    if customer:
        return jsonify(customer_id)
    else:
        return jsonify({'error': 'Tour not found'}), 404