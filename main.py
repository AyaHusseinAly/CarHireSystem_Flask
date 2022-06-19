from controllers.customer_controller import CustomerController
from db_config import *

# adding Customer Resource Route
api.add_resource(CustomerController, '/customers' ,'/customers/<int:id>')


if __name__ == '__main__':

	app.run(debug = True)
