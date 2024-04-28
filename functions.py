# Int value input error net
def spec_input(classtype, value, text):
    while True:
        try:
            value = classtype(input(text))
            return value
        except ValueError:
            print("Invalid input.")

# Function to check balance
def check_balance(cursor, account_number):
    cursor.execute("SELECT balance FROM accounts WHERE account_number = %s", (account_number))
    balance = cursor.fetchone()
    return balance[0] if balance else None

# Function to deposit amount into an account
def deposit(cursor, connection, account_number, amount):
  try:
      cursor.execute("UPDATE accounts SET balance = balance + %s WHERE account_number = %s", (amount, account_number))
      connection.commit()
      return True
  except Exception as e:
      print("Error:", e)
      return False

# Function to withdraw amount from an account
def withdraw(cursor, connection, account_number, amount):
    try:
        cursor.execute("SELECT balance FROM accounts WHERE account_number = %s", (account_number))
        balance = cursor.fetchone()
        if balance and balance[0] >= amount:
            cursor.execute("UPDATE accounts SET balance = balance - %s WHERE account_number = %s", (amount, account_number))
            connection.commit()
            return True
        else:
            print("Insufficient balance.")
            return False
    except Exception as e:
        print("Error:", e)
        return False

# Function to delete an account
def delete_account(cursor, connection, account_number):
    try:
        cursor.execute("DELETE FROM accounts WHERE account_number = %s", (account_number))
        connection.commit()
        return True
    except Exception as e:
        print("Error:", e)
        return False

# Function to modify the PIN of an account
def modify_account(cursor, connection, account_number, new_pin):
    try:
        cursor.execute("UPDATE users SET pin = %s WHERE account_number = %s", (new_pin, account_number))
        connection.commit()
        return True
    except Exception as e:
        print("Error:", e)
        return False

# Other banking functions