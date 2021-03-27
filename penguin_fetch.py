from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)



#MyReadingLists - a list of all reading lists of a user
class Penguin_Books(Resource):
	def get_id(self, book_id):
		return 1 # todo

	def get_name(self, book_name):
		return 1 # todo
