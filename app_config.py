from flask import Flask
from flask_restful import Api
from flask_mysqldb import MySQL

app = Flask(__name__)
api = Api(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3307
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root_1234'
app.config['MYSQL_DB'] = 'CAR_HIRE_SYSTEM'

mysql = MySQL(app)
