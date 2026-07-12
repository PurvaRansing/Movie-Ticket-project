from reports.movie_chart import movie_chart
from reports.booking_chart import booking_chart
from reports.payment_chart import payment_chart

def chart_menu():

    while True:

        print("\n========== Charts ==========")
        print("1. Movie Chart")
        print("2. Booking Chart")
        print("3. Payment Chart")
        print("4. Return to Admin Menu")

        choice = input("Enter your choice : ")

        match choice:

            case "1":
                movie_chart()

            case "2":
                booking_chart()

            case "3":
                payment_chart()

            case "4":
                return

            case _:
                print("Invalid Choice.")