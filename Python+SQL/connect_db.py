import sqlite3 as sql

#creating or connecting to DB
conn = sql.connect('my_friends.db')

#Create a cursor object
c = conn.cursor()

#Executing a command
c.execute("CREATE TABLE Friends (fname TEXT, lname TEXT, age INTEGER, closeness INTEGER);")

#commiting the changes
conn.commit()
#Closing the connection
conn.close()