from flask_restful import Resource
from flask import jsonify, request
from config import mysql


class Customer(Resource):

    # Corresponds to GET request
    def get(self):
        return jsonify({'message': 'success'})

	# Corresponds to POST request
    def post(self):
        try:
            data = request.get_json()
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO CUSTOMERS(full_name, phone, email, country, city, street, building) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                        (data['full_name'], data['phone'], data['email'], data['country'],data['city'], data['street'], data['building'])
                        )
            mysql.connection.commit()
            cur.close()        
            return jsonify({'msg': "customer is created successfully"})

        except Exception as e:
            return jsonify({'error': str(e)})

    # Corresponds to UPDATE request
    def update(self, id):
        data = request.get_json()
        return jsonify({'data': data}), 201

    # Corresponds to DELETE request
    def delete(self, id):
        data = request.get_json()
        return jsonify({'data': data}), 201

