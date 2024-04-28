from database import create_tables, cursor
from variables import account_number, parameters
from functions import check_balance, deposit, withdraw, delete_account, modify_account, spec_input
import inquirer

def ask(message, choices):
    return inquirer.prompt([inquirer.List('',message,choices)])[""]

def main_menu():
    print("Welcome to the Online Banking System")

    choice = ask("Enter your choice",
                 ["1. Check Balance",
                  "2. Deposit",
                  "3. Withdraw",
                  "4. Create Account",
                  "5. Delete Account",
                  "6. Modify Account",
                  "7. Exit"])
    return choice

def execute_choice(choice):
    # Implement balance function
    if choice.find("1") == 0:
        spec_input(int, account_number, "Enter your account number: ")
        balance = check_balance(cursor, account_number,)
        if balance:
            print(f"Your current balance is: ${balance}")
        else:
            print("Account not found.")

    # Implement deposit function
    elif choice.find("2") == 0:
      spec_input(int, account_number, "Enter your account number: ")
      amount = float(input("Enter the amount to deposit: $"))
      success = deposit(cursor, account_number, amount)
      if success:
          print("Deposit successful.")

    # Implement withdraw function
    elif choice.find("3") == 0:
      spec_input(int, account_number, "Enter your account number: ")
      amount = float(input("Enter the amount to withdraw: $"))
      success = withdraw(cursor, account_number, amount)
      if success:
          print("Withdrawal successful.")
      else:
          print("Failed to withdraw.")
    
    # Implement create account function
    elif choice.find("4") == 0:
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        spec_input(int, account_number, "Enter your account number: ")
        parameters = (first_name, last_name, account_number)
        create_tables(parameters)
    
    # Implement delete account function
    elif choice.find("5") == 0:
        spec_input(int, account_number, "Enter the account number to delete: ")
        success = delete_account(cursor, account_number,)
        if success:
            print("Account deleted successfully.")
        else:
            print("Failed to delete account.")
    
    # Implement modify account function
    elif choice.find("6") == 0:
        spec_input(int, account_number, "Enter the account number to modify: ")
        new_pin = input("Enter the new PIN: ")
        success = modify_account(cursor, account_number, new_pin)
        if success:
            print("Account modified successfully.")
        else:
            print("Failed to modify account.")
          
    # Implement exit option
    elif choice.find("7") == 0:
        print("Thank you for using our services. Goodbye!")
        exit()

# Other menu-related functions
