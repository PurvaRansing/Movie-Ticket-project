from authentication.login import login
from authentication.register import register
from authentication.forgot_password import forgot_password

def authentication_menu():

    while True:

        print("\n========== Authentication Menu ==========")
        print("1. Login")
        print("2. Register")
        print("3. Forgot Password")
        print("4. Exit")

        choice = input("Enter your choice: ")

        match choice:

            case "1":
                login()

            case "2":
                register()

            case "3":
                forgot_password()

            case "4":
                print("Thank You!")
                break

            case _:
                print("Invalid Choice")