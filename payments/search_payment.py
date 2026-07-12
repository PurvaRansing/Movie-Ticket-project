from db_connection import get_connection

def search_payment():

    conn = get_connection()
    cursor = conn.cursor()

    while True:

        print("\n========== Search Payment ==========")
        print("1. Search by Payment ID")
        print("2. Search by Booking ID")
        print("3. Search by Payment Method")
        print("4. Back")

        choice = input("Enter your choice : ")

        match choice:

            case "1":

                payment_id = input("Enter Payment ID : ")

                cursor.execute(
                    "SELECT * FROM payments WHERE payment_id = ?",
                    (payment_id,)
                )

            case "2":

                booking_id = input("Enter Booking ID : ")

                cursor.execute(
                    "SELECT * FROM payments WHERE booking_id = ?",
                    (booking_id,)
                )

            case "3":

                print("\nPayment Methods")
                print("1. Cash")
                print("2. UPI")
                print("3. Card")

                method = input("Enter your choice : ")

                if method == "1":
                    payment_method = "Cash"

                elif method == "2":
                    payment_method = "UPI"

                elif method == "3":
                    payment_method = "Card"

                else:
                    print("Invalid Choice.")
                    continue

                cursor.execute(
                    "SELECT * FROM payments WHERE payment_method = ?",
                    (payment_method,)
                )

            case "4":

                conn.close()
                return

            case _:

                print("Invalid Choice.")
                continue

        payments = cursor.fetchall()

        if len(payments) == 0:

            print("\nNo Payment Found.")
            continue

        print("\n=========================================================================================")
        print("Payment ID\tBooking ID\tMethod\t\tDate\t\tAmount\tStatus")
        print("=========================================================================================")

        for payment in payments:

            print(
                payment[0], "\t",
                payment[1], "\t",
                payment[2], "\t",
                payment[3], "\t",
                payment[4], "\t",
                payment[5]
            )

        print("=========================================================================================")

    conn.close()