from flask_restful import Resource
from flask import jsonify, request

from models.customer_model import Customer

class CustomerController(Resource):

    # Corresponds to GET request to route: '/customers/<int:id>'
    def get(self, id):
        try:
            customer_obj = Customer.find(id)
            if not customer_obj:
                response = jsonify({'data': f'Customer with id: {id} Not Found'})
                response.status_code = 404
                return response  

            response = jsonify({'data': customer_obj.__dict__})
            response.status_code = 200
            return response  

        except Exception as e:
            response = jsonify({'error': str(e)})
            response.status_code = 500
            return response  

	# Corresponds to POST request to route: '/customers'
    def post(self):
        try:
            data = request.get_json()
            customer_obj = Customer.create(data)
            response = jsonify({'data': customer_obj.__dict__})
            response.status_code = 201
            return response  

        except Exception as e:
            response = jsonify({'error': str(e)})
            response.status_code = 500
            return response  

    # Corresponds to PUT request to route: '/customers/<int:id>'
    def put(self, id):
        try:
            data = request.get_json()
            updated = Customer.update(id, data)
            msg = "customer updated successfully"
            if not updated:
                msg = f'No updates :: either Customer not found or it has same provided data'

            response = jsonify({'data': msg})
            response.status_code = 200
            return response  

        except Exception as e:
            response = jsonify({'error': str(e)})
            response.status_code = 500
            return response     

    # Corresponds to DELETE request to route: '/customers/<int:id>'
    def delete(self, id):
        try:
            deleted = Customer.delete(id)
            if not deleted:
                response = jsonify({'data': f'Customer with id: {id} Not Found'})
                response.status_code = 404
                return response 

            msg = "customer deleted successfully"
            response = jsonify({'data': msg})
            response.status_code = 200
            return response  

        except Exception as e:
            response = jsonify({'error': str(e)})
            response.status_code = 500
            return response  
