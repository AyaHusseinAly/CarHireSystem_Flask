from flask_restful import Resource
from flask import jsonify, request

from models.vehicle_model import Vehicle

def Error_Handler(func):
    def Inner_Function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Exception::{func.__module__}::{func.__qualname__}::{func.__name__}::{str(e)}")
            response = jsonify({'error': str(e)})
            response.status_code = 500
            return response  
    return Inner_Function

class VehiclesController(Resource):

    # Corresponds to GET request to route: '/vehicles/<int:id>'
    @Error_Handler
    def get(self, id):
        vehicle_obj = Vehicle.find(id)
        if not vehicle_obj:
            response = jsonify({'data': f'Vehicle with id: {id} Not Found'})
            response.status_code = 404
            return response  

        response = jsonify({'data': vehicle_obj.__dict__})
        response.status_code = 200
        return response  


	# Corresponds to POST request to route: '/vehicles'
    @Error_Handler
    def post(self):
        data = request.get_json()
        vehicle_obj = Vehicle.create(data)
        response = jsonify({'data': vehicle_obj.__dict__})
        response.status_code = 201
        return response  

    # Corresponds to PUT request to route: '/vehicles/<int:id>'
    @Error_Handler
    def put(self, id):
        data = request.get_json()
        updated = Vehicle.update(id, data)
        msg = "vehicle updated successfully"
        if not updated:
            msg = f'No updates :: either Vehicle not found or it has same provided data'

        response = jsonify({'data': msg})
        response.status_code = 200
        return response  

    # Corresponds to DELETE request to route: '/vehicles/<int:id>'
    @Error_Handler
    def delete(self, id):
        deleted = Vehicle.delete(id)
        if not deleted:
            response = jsonify({'data': f'Vehicle with id: {id} Not Found'})
            response.status_code = 404
            return response 

        msg = "vehicle deleted successfully"
        response = jsonify({'data': msg})
        response.status_code = 200
        return response  

