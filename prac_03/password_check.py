def main():
    password = input("Enter the password \n>>> ")

    hide_password(password)
    password_guess(password)


def hide_password(password):
    hidden_password = "*" * len(password)
    print("Password: " + hidden_password)


def password_guess(password):
    guess = input("Enter the password \n>>> ")
    while guess != password:
        print("Incorrect password. Please try again.")
        guess = input("Enter the password \n>>> ")
    print("Password correct. Logging you in.")


main()
