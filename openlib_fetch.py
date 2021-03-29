import requests
import json

class Booksearch():
    def booknamesearch(self,title):
        response_book = requests.get("http://openlibrary.org/search.json?title="+title)
        json_response = response_book.json()
        docs = json_response["docs"]
        booklist = []
        for line in docs:
            booklist.append(line["title"])
    
        return booklist
    
    
    def bookauthorsearch(self,author):
        response_book = requests.get("http://openlibrary.org/search.json?author="+author)
        json_response = response_book.json()
        docs = json_response["docs"]
        booklist = []
        for line in docs:
            booklist.append(line["title"])
    
        return booklist