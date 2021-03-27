from flask import Flask
from flask_restful import Api, Resource, reqparse
import penguin_fetch as pf
import mysql.connector


app = Flask(__name__)
api = Api(app)

read_list = {
	'list1' : ['book1', 'book2'],
	'list2' : ['book3', 'book4']
}

class mySQLDB():

	def db_connect():
		#connection string here
		mydb = mysql.connector.connect(
  		host="localhost",
  		user="yourusername",
  		password="yourpassword",
  		database="mydatabase"
	)

	mycursor = mydb.cursor()


#MyReadingLists - a list of all reading lists of a user
class MyReadingLists(Resource):

	#gets all reading lists of a user
	def get(self, user_id):

		#fetch record from DB here and return the list.
		return read_list

	def abort_if_list_not_exist(listid):
	    if listid not in read_list:
		    abort(404, message = "Reading list {} does not exist.".format(listid))
            return 1   # check

    #create a new list
    def post(self, user_id, body):
    	#insert record into reading list table.
        response = ""
        return response		#number, message

    #delete an existing list
    def delete(self, user_id):
    	#delete record from reading list table.
        response = ""
        return response    #number, message

    #update the list.
    def put(self, user_id):
    	#list rename
        response = ""
        return response		#number, message       

#ReadingList - book names in a particular reading list
class Books(Resource):
	def get(self, listid):
		abort_if_list_not_exist(listid)

		#get all the books from the given reading list - from DB.
		return read_list[listid]

	def deleteBookFromList(self, listid):
		abort_if_list_not_exist(listid)
		del read_list[listid]
		return '',204

	def put(self, listid):
		read_list[listid] = []
		return '', 201

	def addBookToList(self, listid):
		#add new book to the list.
		return '', 201

	def getPenguinBooks(self, listid):
        # call penguin_fetch here
		return '', 201





api.add_resource(MyReadingLists, "/readinglist/viewalllists")
api.add_resource(ReadingList, "/readinglist/viewlist/<listid>")

if __name__ == "__main__":
	app.run(debug=True)
