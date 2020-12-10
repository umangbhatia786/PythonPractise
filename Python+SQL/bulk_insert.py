import sqlite3 as sql
from csv import reader


#creating or connecting to DB
conn = sql.connect('dog_db.db')

#Create a cursor object
c = conn.cursor()

#Executing a command
#c.execute("CREATE TABLE Friends (fname TEXT, lname TEXT, age INTEGER, closeness INTEGER);")

people = [
    ('Josh','Husky',7),
    ('Peter','Pug',9)
]

insert_query = f"INSERT INTO Dog VALUES (?,?,?)"
c.executemany(insert_query, people)

#commiting the changes
conn.commit()
#Closing the connection
conn.close()