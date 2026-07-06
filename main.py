from authentication.login import admin_login, customer_login
from authentication.register import register
from authentication.forgot_password import forgot_password
from movies.movie_menu import movie_menu
from theatres.theatre_menu import theatre_menu
from shows.show_menu import show_menu
from bookings.booking_menu import booking_menu
from payments.payment_menu import payment_menu
from reports.report_menu import report_menu


def admin_menu():

    while True:

        print("\n========== Admin Menu ==========")
        print("1. Movie Management")
        print("2. Theatre Management")
        print("3. Show Management")
        print("4. Booking Management")
        print("5. Payment Management")
        print("6. Reports")
        print("7. Logout")

        choice = input("Enter your choice : ")

        match choice:

            case "1":
                movie_menu()

            case "2":
                theatre_menu()

            case "3":
                show_menu()

            case "4":
                booking_menu()

            case "5":
                payment_menu()

            case "6":
                report_menu()

            case "7":
                print("Logged Out Successfully.")
                break

            case _:
                print("Invalid Choice")


def customer_menu():

    while True:

        print("\n========== Customer Menu ==========")
        print("1. View Movies")
        print("2. View Shows")
        print("3. Book Ticket")
        print("4. View My Bookings")
        print("5. Cancel Booking")
        print("6. Logout")

        choice = input("Enter your choice : ")

        match choice:

            case "1":
                print("View Movies")

            case "2":
                print("View Shows")

            case "3":
                print("Book Ticket")

            case "4":
                print("View My Bookings")

            case "5":
                print("Cancel Booking")

            case "6":
                print("Logged Out Successfully.")
                break

            case _:
                print("Invalid Choice")


def main():

    while True:

        print("\n========== CINEFLOW ==========")
        print("1. Admin Login")
        print("2. Customer Login")
        print("3. Customer Register")
        print("4. Forgot Password")
        print("5. Exit")

        choice = input("Enter your choice : ")

        match choice:

            case "1":

                if admin_login():
                    admin_menu()

            case "2":

                if customer_login():
                    customer_menu()

            case "3":

                register()

            case "4":

                forgot_password()

            case "5":

                print("Thank You!")
                break

            case _:

                print("Invalid Choice")


main()