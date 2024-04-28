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
def create_tables(parameters = tuple()):
  sql = "INSERT INTO users (id, pin, balance) VALUES (%s, %s, %s)"
  cursor.execute(sql, parameters)

# Insert initial data
def insert_initial_data():
  cursor.execute("INSERT INTO users (id, pin, is_admin) VALUES ('123456', '1234', 1)")
  connection.commit()

# Other database functions