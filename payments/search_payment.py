from db_connection import get_connection
from rich.table import Table
from rich.console import Console

console = Console()


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


        if choice == "1":

            payment_id = input("Enter Payment ID : ")

            cursor.execute(
                "SELECT * FROM payments WHERE payment_id=?",
                (payment_id,)
            )


        elif choice == "2":

            booking_id = input("Enter Booking ID : ")

            cursor.execute(
                "SELECT * FROM payments WHERE booking_id=?",
                (booking_id,)
            )


        elif choice == "3":

            print("\n1. Cash")
            print("2. UPI")
            print("3. Card")

            method = input("Enter Payment Method : ")

            if method == "1":
                payment_method = "Cash"

            elif method == "2":
                payment_method = "UPI"

            elif method == "3":
                payment_method = "Card"

            else:
                print("Invalid Choice")
                continue


            cursor.execute(
                "SELECT * FROM payments WHERE payment_method=?",
                (payment_method,)
            )


        elif choice == "4":

            break


        else:

            print("Invalid Choice")
            continue



        payments = cursor.fetchall()


        if len(payments) == 0:

            print("\nNo Payment Found.")
            continue



        table = Table(title="Payment Details")


        table.add_column("Payment ID")
        table.add_column("Booking ID")
        table.add_column("Method")
        table.add_column("Date")
        table.add_column("Amount")
        table.add_column("Status")


        for payment in payments:

            table.add_row(
                str(payment[0]),
                str(payment[1]),
                str(payment[2]),
                str(payment[3]),
                str(payment[4]),
                str(payment[5])
            )


        console.print(table)


    conn.close()