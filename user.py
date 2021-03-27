# import sqlite3


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()



class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    def create_user(username, password):
        sql = "INSERT INTO Users (name, address) VALUES (%s, %s)"
        val = ("John", "Highway 21")
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")

    @classmethod
    def find_by_username (cls, username):

        connection = mysql.connector.connect(
                host="localhost",
                user="yourusername",
                password="yourpassword",
                database="mydatabase")

        # connection = sqlite3.connect('data.db')
        
        cursor=connection.cursor()

        query = "SELECT * FROM users WHERE username=%s"

        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row is not None:
            user = cls(row[0],row[1],row[2])
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id (cls, _id):
        connection = sqlite3.connect('data.db')
        cursor=connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row is not None:
            user = cls(row[0],row[1],row[2])
        else:
            user = None

        connection.close()
        return user
