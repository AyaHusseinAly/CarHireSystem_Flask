from flask_restful import Resource
from flask import jsonify, request

from models.customer_model import Customer
from commons.error_handler import Error_Handler

class CustomersController(Resource):

    # Corresponds to GET request to route: '/customers/<int:id>'
    @Error_Handler
    def get(self, id):
        customer_obj = Customer.find(id)
        if not customer_obj:
            response = jsonify({'data': f'Customer with id: {id} Not Found'})
            response.status_code = 404
            return response  

        response = jsonify({'data': customer_obj.__dict__})
        response.status_code = 200
        return response  


	# Corresponds to POST request to route: '/customers'
    @Error_Handler
    def post(self):
        data = request.get_json()
        customer_obj = Customer.create(data)
        response = jsonify({'data': customer_obj.__dict__})
        response.status_code = 201
        return response  

    # Corresponds to PUT request to route: '/customers/<int:id>'
    @Error_Handler
    def put(self, id):
        data = request.get_json()
        updated = Customer.update(id, data)
        msg = "customer updated successfully"
        if not updated:
            msg = f'No updates :: either Customer not found or it has same provided data'

        response = jsonify({'data': msg})
        response.status_code = 200
        return response  

    # Corresponds to DELETE request to route: '/customers/<int:id>'
    @Error_Handler
    def delete(self, id):
        deleted = Customer.delete(id)
        if not deleted:
            response = jsonify({'data': f'Customer with id: {id} Not Found'})
            response.status_code = 404
            return response 

        msg = "customer deleted successfully"
        response = jsonify({'data': msg})
        response.status_code = 200
        return response  

