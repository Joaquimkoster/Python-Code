import os                                                                                           # imports the os module to work with files and check if they exist

FILE_NAME = "Registration.txt"                                                                      # creates a constant with the name of the file where users will be stored


def load_users():                                                                                   # defines the function responsible for loading users from the file
    users = {}                                                                                      # creates an empty dictionary to store usernames and passwords

    if not os.path.exists(FILE_NAME):                                                               # checks if the file does not exist in the system
        return users                                                                                # if the file doesn't exist, returns the empty dictionary

    with open(FILE_NAME, "r") as file:                                                              # opens the file in read mode ("r") and ensures it will close automatically
        for line in file:                                                                           # loops through every line in the file
            username, password = line.strip().split(",")                                            # removes spaces/newlines and splits username and password by comma
            users[username] = password                                                              # stores the username and password inside the dictionary

    return users                                                                                    # returns the dictionary containing all loaded users


def save_users(users):                                                                              # defines the function that saves users into the file
    with open(FILE_NAME, "w") as file:                                                              # opens the file in write mode ("w"), replacing old content
        for username, password in users.items():                                                    # loops through every username and password in the dictionary
            file.write(f"{username},{password}\n")                                                  # writes each username and password separated by a comma into the file


def register():                                                                                     # defines the function responsible for registering new users

    print("")                                                                                       # prints an empty line for visual spacing
    print("=== USER REGISTRATION ===")                                                              # displays the registration screen title

    username = input("Enter your username: ")                                                       # asks the user to enter a username
    password = input("Enter your password: ")                                                       # asks the user to enter a password

    users = load_users()                                                                            # calls the load_users function to load existing users

    if username in users:                                                                           # checks if the username already exists
        print("User already exists!")                                                               # informs that the user is already registered
        return                                                                                      # stops the function to prevent duplication

    users[username] = password                                                                      # adds the new username and password to the dictionary

    save_users(users)                                                                               # saves the updated dictionary to the file

    print("Registration saved successfully!!!")                                                     # displays a success message


def login():                                                                                        # defines the function responsible for user login

    print("")                                                                                       # prints an empty line for better readability
    print("=== USER LOGIN ===")                                                                     # displays the login screen title

    username = input("Enter your username: ")                                                       # asks the user to type the username
    password = input("Enter your password: ")                                                       # asks the user to type the password

    users = load_users()                                                                            # loads all saved users

    if username not in users:                                                                       # checks if the username does not exist
        print("User not found.")                                                                    # informs that the user was not found
        return                                                                                      # stops the function

    if users[username] == password:                                                                 # checks if the entered password matches the stored password
        print("Login successful!!!")                                                                # informs that login was successful
    else:                                                                                           # if the password is incorrect
        print("Incorrect password.")                                                                # informs that the password is wrong


def delete_user():                                                                                  # defines the function responsible for deleting a user

    print("")                                                                                       # prints an empty line
    print("=== DELETE USER ===")                                                                    # displays the delete user screen title

    username = input("Enter the username to delete: ")                                              # asks for the username that will be deleted
    password = input("Enter the password: ")                                                        # asks for the password to confirm identity

    users = load_users()                                                                            # loads all users from the system

    if username not in users:                                                                       # checks if the username does not exist
        print("User not found.")                                                                    # informs that the user was not found
        return                                                                                      # stops the function

    if users[username] != password:                                                                 # checks if the entered password is incorrect
        print("Incorrect password.")                                                                # informs that the password is wrong
        return                                                                                      # stops the function

    del users[username]                                                                             # removes the user from the dictionary

    save_users(users)                                                                               # saves the updated dictionary back to the file

    print("User deleted successfully.")                                                             # displays a success message


while True:                                                                                         # creates an infinite loop to keep the system running

    print("")                                                                                       # prints an empty line
    print("===== SYSTEM =====")                                                                     # displays the system title
    print("1) Register")                                                                            # shows option 1 to register a user
    print("2) Login")                                                                               # shows option 2 to login
    print("3) Delete User")                                                                         # shows option 3 to delete a user
    print("4) Exit")                                                                                # shows option 4 to exit the system

    option = input("Choose an option: ")                                                            # asks the user to choose an option

    if option == "1":                                                                               # checks if option 1 was selected
        register()                                                                                  # calls the register function

    elif option == "2":                                                                             # checks if option 2 was selected
        login()                                                                                     # calls the login function

    elif option == "3":                                                                             # checks if option 3 was selected
        delete_user()                                                                               # calls the delete_user function

    elif option == "4":                                                                             # checks if option 4 was selected
        print("Exiting the system...")                                                              # displays exit message
        break                                                                                       # breaks the loop and ends the program

    else:                                                                                           # if the user types anything else
        print("Invalid option, please try again.")                                                  # informs the user that the option is invalid