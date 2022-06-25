from marshmallow import Schema, fields, ValidationError
from flask import jsonify

class VehicleSchema(Schema):
    plate_not = fields.Integer(required=True)
    model = fields.String(required=True)
    category = fields.String(required=True)



def validate_vehicle_data(request_data):
    try:
        schema = VehicleSchema()
        schema.load(request_data)

        return None
    except ValidationError as err:
        response = jsonify(err.messages)
        response.status_code = 400
        return response  
