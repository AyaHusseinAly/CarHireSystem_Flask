from flask import Flask, jsonify, request
from controllers.customer_controller import Customer
from config import *

# adding Routes
# api.add_resource(Customer(app), '/customers/<int:id>')
api.add_resource(Customer, '/customers')


if __name__ == '__main__':

	app.run(debug = True)
