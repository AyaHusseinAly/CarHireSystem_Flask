from controllers.customer_controller import CustomerController
from db_config import *

# adding Routes
api.add_resource(CustomerController, '/customers' ,'/customers/<int:id>')
# api.add_resource(Customer, '/customers')


if __name__ == '__main__':

	app.run(debug = True)
