from controllers.customers_controller import CustomersController
from controllers.vehicles_controller import VehiclesController
from app_config import *

# adding Customer Resource Route
api.add_resource(CustomersController, '/customers' ,'/customers/<int:id>')
api.add_resource(VehiclesController, '/vehicles' ,'/vehicles/<int:id>')


if __name__ == '__main__':

	app.run(debug = True)
