# pyos.py

# Dictionary to store user credentials
users = {
    "user1": "password1",
    "user2": ""  # Empty password for user2
}

def login(user):
    if user in users:
        password = input("Enter your password for {}: ".format(user))
        if password == users[user]:
            print("Login successful. Welcome, {}!".format(user))
            # Add your logic for what happens after login
        else:
            print("Incorrect password. Please try again.")
    else:
        print("User '{}' does not exist.".format(user))

def main():
    print("Welcome to PyOS!")
    while True:
        command = input("Enter a command (login %user%, exit): ")
        if command.startswith("login "):
            user = command.split(" ")[1]
            login(user)
        elif command == "exit":
            print("Exiting PyOS.")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
