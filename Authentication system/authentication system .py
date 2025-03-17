user_credentials = {}

def register_user():
    username = input("Enter username: ")

    if username in user_credentials:
        print("Username already exists. Please choose another username")
    else:
        password = input("Enter password: ")
        user_credentials[username] = password
        print("User registered successfully")
def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in user_credentials and user_credentials[username] == password:
         print("Welcome Back")
    else:
         print("Invalid username or password. Please try again.")


def authentication_system():
    while True:
        print("Basic Authentication System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        option = input("Enter your choice: ")

        if option == "1":
           register_user()
        elif option == "2":
           login_user()
        elif option == "3":
           print("Exiting the system...")
           break 
        else:
           print("Invalid choice. Please try again.")

authentication_system()