import sqlite3 as sql
from csv import reader


#creating or connecting to DB
conn = sql.connect('my_friends.db')

#Create a cursor object
c = conn.cursor()

#Executing a command
#c.execute("CREATE TABLE Friends (fname TEXT, lname TEXT, age INTEGER, closeness INTEGER);")
insert_query = f"INSERT INTO Friends VALUES (?,?,?,?)"
csv_path = "Python+SQL\insert_data.csv"

#Redading CSV Data and executing the insert statements
with open(csv_path) as f:
    csv_reader = reader(f)
    csv_rows = list(csv_reader)

for i in range (1, len(csv_rows)):
    c.execute(insert_query, (csv_rows[i][0],csv_rows[i][1],int(csv_rows[i][2]),int(csv_rows[i][3])))
#commiting the changes
conn.commit()
#Closing the connection
conn.close()