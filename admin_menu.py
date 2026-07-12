from movies.movie_menu import movie_menu
from theatres.theatre_menu import theatre_menu
from shows.show_menu import show_menu
from bookings.booking_menu import booking_menu
from payments.payment_menu import payment_menu
from reports.report_menu import report_menu
from reports.chart_menu import chart_menu


def admin_menu():

    while True:

        print("\n========== ADMIN MENU ==========")
        print("1. Movie Management")
        print("2. Theatre Management")
        print("3. Show Management")
        print("4. Booking Management")
        print("5. Payment Management")
        print("6. Reports")
        print("7. Charts")
        print("8. Logout")

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
                chart_menu()

            case "8":
                print("\nAdmin Logged Out Successfully.")
                break

            case _:
                print("Invalid Choice.")