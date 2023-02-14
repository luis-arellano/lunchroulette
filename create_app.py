from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:rockclimber1!@database-1.ciiowaujelgi.us-west-2.rds.amazonaws.com:3306/lunchroulette'

db = SQLAlchemy(app)

# mysql -h database-1.ciiowaujelgi.us-west-2.rds.amazonaws.com -P 3306 -u root -p
