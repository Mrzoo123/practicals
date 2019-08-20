def main():
    password = input("Enter the password \n>>> ")
    hidden_password = "*" * len(password)

    print("Password: " + hidden_password)

    password_guess(password)


def password_guess(password):

    guess = input("Enter the password \n>>> ")
    while guess != password:
        print("Incorrect password. Please try again.")
        guess = input("Enter the password \n>>> ")
    print("Password correct. Logging you in.")


main()
