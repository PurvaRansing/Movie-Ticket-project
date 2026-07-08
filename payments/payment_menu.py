from payments.make_payment import make_payment
from payments.view_payment import view_payments
from payments.search_payment import search_payment


def payment_menu():

    while True:

        print("\n========== Payment Management ==========")
        print("1. Make Payment")
        print("2. View Payments")
        print("3. Search Payment")
        print("4. Return to Admin Menu")

        choice = input("Enter your choice : ")

        match choice:

            case "1":
                make_payment()

            case "2":
                view_payments()

            case "3":
                search_payment()

            case "4":
                return

            case _:
                print("Invalid Choice.")