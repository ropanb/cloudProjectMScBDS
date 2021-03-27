from flask import Flask
from flask_restful import Api, Resource, reqparse
import penguin_fetch as pf

app = Flask(__name__)
api = Api(app)

read_list = {
	'list1' : ['book1', 'book2'],
	'list2' : ['book3', 'book4']
}

#MyReadingLists - a list of all reading lists of a user
class MyReadingLists(Resource):
	def get(self, user_id):
		return read_list

	def abort_if_list_not_exist(listid):
	    if listid not in read_list:
		    abort(404, message = "Reading list {} does not exist.".format(listid))
            return 1   # check

    def post(self, user_id, body):
        response = ""
        return response

    def delete(self, user_id):
        response = ""
        return response    

     def put(self, user_id):
        response = ""
        return response       

#ReadingList - book names in a particular reading list
class Books(Resource):
	def get(self, listid):
		abort_if_list_not_exist(listid)
		return read_list[listid]

	def delete(self, listid):
		abort_if_list_not_exist(listid)
		del read_list[listid]
		return '',204

	def put(self, listid):
		read_list[listid] = []
		return '', 201

	def post(self, listid):
        # call penguin_fetch here
		return '', 201

#maintenance of users
class Users(Resource):

	def get(self):
		return read_list

	def get_user(self, user_id):
		return read_list        

    def post(self, user_id):
        response = ""
        return response

    def delete(self, user_id):
        response = ""
        return response    

     def put(self, user_id):
        response = ""
        return response       



	return



api.add_resource(MyReadingLists, "/readinglist/viewalllists")
api.add_resource(ReadingList, "/readinglist/viewlist/<listid>")

if __name__ == "__main__":
	app.run(debug=True)
