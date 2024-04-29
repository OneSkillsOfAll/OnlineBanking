from database import create_tables

# Function to check balance
def check_balance(cursor, id):
    cursor.execute("SELECT balance FROM users WHERE id = %s", (id,))
    balance = cursor.fetchone()
    return balance[0] if balance else None

# Function to deposit amount into an account
def deposit(cursor, connection, id, amount):
  try:
      cursor.execute("UPDATE users SET balance = balance + %s WHERE id = %s", (amount, id,))
      connection.commit()
      return True
  except Exception as e:
      print("Error:", e)
      return False

# Function to withdraw amount from an account
def withdraw(cursor, connection, id, amount):
    try:
        cursor.execute("SELECT balance FROM users WHERE id = %s", (id,))
        balance = cursor.fetchone()
        if balance and balance[0] >= amount:
            cursor.execute("UPDATE users SET balance = balance - %s WHERE id = %s", (amount, id,))
            connection.commit()
            return True
        else:
            print("Insufficient balance.")
            return False
    except Exception as e:
        print("Error:", e)
        return False

#Function to create an account
def create_account(para):
    create_tables(para)

# Function to delete an account
def delete_account(cursor, connection, id):
    try:
        cursor.execute("DELETE FROM users WHERE id = %s", (id,))
        connection.commit()
        return True
    except Exception as e:
        print("Error:", e)
        return False

# Function to modify the PIN of an account
def modify_account(cursor, connection, id, new_pin):
    try:
        cursor.execute("UPDATE users SET pin = %s WHERE id = %s", (new_pin, id,))
        connection.commit()
        return True
    except Exception as e:
        print("Error:", e)
        return False

# Other banking functions

# Int value input error net
def spec_input(classtype, value, text):
    while True:
        try:
            value = classtype(input(text))
            return value
        except ValueError:
            print("Invalid input.")