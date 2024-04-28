import random
import mysql.connector
from variables import parameters

credentials = {
  "host": "localhost",
  "user": "root",
  "database": "demo",
  "password": "MySQLSucks0!"
}
# Connect to MySQL
connection = mysql.connector.connect(**credentials, autocommit = True)

# Create cursor
cursor = connection.cursor()

# Create tables
def create_tables(para = tuple()):
  sql = "INSERT INTO users (id, pin, balance, is_admin) VALUES (%s, %s, %s, %s)"
  cursor.execute(sql, para,)

# Insert initial data
def insert_initial_data():
  genID = random.randint(1, 99999)
  cursor.execute("INSERT INTO users (id, pin, balance, is_admin) VALUES ('genID', '1234', '1000', false)")
  connection.commit()

# Other database functions