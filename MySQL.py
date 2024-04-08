import mysql.connector

 

connection = mysql.connector.connect(user = ‘username’, database = ‘database_name’, password = ‘password’)

 

connection.close()