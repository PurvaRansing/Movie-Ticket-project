from authentication.admin_login import admin_login
from authentication.customer_login import customer_login
from authentication.register import register
from authentication.forgot_password import forgot_password

from admin_menu import admin_menu
from customer_menu import customer_menu


def main():

    while True:

        print("\n========== CINEFLOW ==========")
        print("1. Admin Login")
        print("2. Customer Login")
        print("3. Customer Register")
        print("4. Forgot Password")
        print("5. Exit")

        choice = input("Enter your choice : ")

        if choice == "1":

            if admin_login():
                admin_menu()

        elif choice == "2":

            if customer_login():
                customer_menu()

        elif choice == "3":

            register()

        elif choice == "4":

            forgot_password()

        elif choice == "5":

            print("Thank You!")
            break

        else:

            print("Invalid Choice")


if __name__ == "__main__":
    main()