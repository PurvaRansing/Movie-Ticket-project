from db_connection import get_connection

def view_payments():

    conn = get_connection()
    cursor = conn.cursor()

    while True:

        print("\n========== View Payments ==========")
        print("1. View All Payments")
        print("2. Sort by Amount")
        print("3. Sort by Payment Date")
        print("4. Back")

        choice = input("Enter your choice : ")

        match choice:

            case "1":

                cursor.execute("SELECT * FROM payments")

            case "2":

                cursor.execute(
                    "SELECT * FROM payments ORDER BY amount"
                )

            case "3":

                cursor.execute(
                    "SELECT * FROM payments ORDER BY payment_date"
                )

            case "4":

                conn.close()
                return

            case _:

                print("Invalid Choice.")
                continue

        payments = cursor.fetchall()

        if len(payments) == 0:

            print("\nNo Payments Found.")
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