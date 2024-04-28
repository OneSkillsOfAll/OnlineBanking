"""import mysql.connector

connection = mysql.connector.connect(host = 'localhost', user = 'root', database = 'demo', password = 'MySQLSucks0!', autocommit = True)

# Insert into a table with an auto-increment column (id) by
# omitting the column from the explicit column list
cursor = connection.cursor()
sql = "INSERT INTO users (first_name, last_name, pin) VALUES (%s, %s, %s)"
parameters = ("Arsha", "S", '1234')
cursor.execute(sql, parameters) 

# Get the auto-increment ID of the last row inserted
cursor.execute("SELECT LAST_INSERT_ID()")
result = cursor.fetchone()
id = result[0]
print(f"New id is {id}")

cursor = connection.cursor()

testQuery = ('SELECT * FROM users')

cursor.execute(testQuery)

for item in cursor:
    print(item)

cursor.close()

connection.close()"""