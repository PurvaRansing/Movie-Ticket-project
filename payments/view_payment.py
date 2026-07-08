def view_payments():
    while True:
        print("\n========== VIEW PAYMENTS ==========")
        print("1. View All Payments")
        print("2. Sort by Amount")
        print("3. Sort by Date")
        print("4. Back")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                print("Displaying All Payments...")

            case "2":
                print("Displaying Payments Sorted by Amount...")

            case "3":
                print("Displaying Payments Sorted by Date...")

            case "4":
                print("Returning to Payment Menu...")
                break

            case _:
                print(" Invalid Choice! Please try again.")

if __name__ == "__main__":
    view_payments()