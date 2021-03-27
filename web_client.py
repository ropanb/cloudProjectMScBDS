import requests
from pprint import pprint

base_url = "http://127.0.0.1:5000/"

print("Fetching all reading lists...")
#GET request to fetch all reading lists of a user.
response = requests.get(base_url + "readinglist/viewalllists")
if response.ok:
	results = response.json()
else:
	print(response.reason)

pprint(results)


print("Fetching only list2...")
#GET request to fetch a particular reading list of a user.

list_name = "list2"

response = requests.get(base_url + "readinglist/viewlist/{}".format(list_name))
if response.ok:
	results = response.json()
else:
	print(response.reason)

pprint(results)