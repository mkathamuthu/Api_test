from flask import Flask, request
from flask_restful import Resource,Api
from sqlalchemy import create_engine
from json import dumps
#from flask.ext.jsonpify import jsonify

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)

class Employee(Resource):
	def get(self):
		conn = db_connect.connect()
		query = conn.execute("select * from employees")
		return {'employees':[i[0] for i in query.cursor.fetchall()]}

class Tracks(Resource):
	def get(self):
		conn = db_connect.connect()
		query = conn.execute("select trackid,name,composer,unitprice from tracks;")
		result = {'data' : [dict(zip(tuple(query.keys()),i))for i in query.cursor]}
		return result

api.add_resource(Employee,'/employees')
api.add_resource(Tracks, '/tracks')

if __name__ == '__main__':
	app.run(port='5002')