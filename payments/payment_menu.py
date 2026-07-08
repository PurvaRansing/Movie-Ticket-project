from make_payment import make_payment
from view_payment import view_payments
from search_payment import search_payments


def payment_menu():
    while True:
        print("\n========== PAYMENT MENU ==========")
        print("1. Make Payment")
        print("2. View Payments")
        print("3. Search Payments")
        print("4. Back")
        print("5. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                make_payment()

            case "2":
                view_payments()

            case "3":
                search_payments()

            case "4":
                print("Returning to Main Menu...")
                break

            case "5":
                print("Thank You!")
                break

            case _:
                print(" Invalid Choice! Please try again.")


if __name__ == "__main__":
    payment_menu()