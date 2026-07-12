from reports.movie_report import movie_report
from reports.booking_report import booking_report
from reports.payment_report import payment_report


def report_menu():

    while True:

        print("\n========== Reports ==========")
        print("1. Movie Report")
        print("2. Booking Report")
        print("3. Payment Report")
        print("4. Return to Admin Menu")

        choice = input("Enter your choice : ")

        match choice:

            case "1":
                movie_report()

            case "2":
                booking_report()

            case "3":
                payment_report()

            case "4":
                return

            case _:
                print("Invalid Choice.")