from menu import main_menu, execute_choice

def main():
    while True:
        choice = main_menu()
        execute_choice(choice)

if __name__ == "__main__":
    main()
