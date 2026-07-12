from movies.view_movie import view_movies
#from shows.view_show import view_show
from bookings.book_ticket import book_ticket
from bookings.view_booking import view_bookings
from bookings.search_booking import search_booking
from bookings.cancel_booking import cancel_booking
from payments.make_payment import make_payment


def customer_menu():

    while True:

        print("\n========== CUSTOMER MENU ==========")
        print("1. View Movies")
        print("2. View Shows")
        print("3. Book Ticket")
        print("4. View My Bookings")
        print("5. Search My Booking")
        print("6. Cancel Booking")
        print("7. Make Payment")
        print("8. Logout")

        choice = input("Enter your choice : ")

        match choice:

            case "1":
                view_movies()

            # case "2":
            #     view_show()

            case "3":
                book_ticket()

            case "4":
                view_bookings()

            case "5":
                search_booking()

            case "6":
                cancel_booking()

            case "7":
                make_payment()

            case "8":
                print("\nCustomer Logged Out Successfully.")
                break

            case _:
                print("Invalid Choice.")