import mysql.connector

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
parameters = ('', '', '')
def create_tables():
  sql = "INSERT INTO users (first_name, last_name, pin) VALUES (%s, %s, %s)"
  cursor.execute(sql, parameters)

# Insert initial data
def insert_initial_data():
    cursor.execute("INSERT INTO users (account_number, pin, is_admin) VALUES ('123456', '1234', 1)")
    connection.commit()

# Other database functions

