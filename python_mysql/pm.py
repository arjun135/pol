import mysql.connector

db=mysql.connector.connect(

host="localhost",
user="root",
password="dataeaze100"


)

mycursor=db.cursor()

mycursor.execute("show databases")


#---------
