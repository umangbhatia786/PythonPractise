import sqlite3 as sql
from csv import reader


#creating or connecting to DB
conn = sql.connect('my_friends.db')

#Create a cursor object
c = conn.cursor()

#Executing a command

c.execute("SELECT * FROM Friends WHERE fname IS 'Pri'")
'''for result in c:
    print(result)'''
print(c.fetchall())
#commiting the changes
conn.commit()
#Closing the connection
conn.close()