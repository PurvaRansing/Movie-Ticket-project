from db_connection import get_connection
from datetime import datetime

def make_payment():

    conn = get_connection()
    cursor = conn.cursor()

    while True:

        print("\n========== Make Payment ==========")
        print("1. Cash Payment")
        print("2. UPI Payment")
        print("3. Card Payment")
        print("4. Back")

        choice = input("Enter your choice : ")

        if choice == "1":
            payment_method = "Cash"

        elif choice == "2":
            payment_method = "UPI"

        elif choice == "3":
            payment_method = "Card"

        elif choice == "4":
            conn.close()
            return

        else:
            print("Invalid Choice.")
            continue

        booking_id = input("Enter Booking ID : ")

        cursor.execute(
            "SELECT * FROM bookings WHERE booking_id = ?",
            (booking_id,)
        )

        booking = cursor.fetchone()

        if booking is None:

            print("Booking ID Not Found.")
            continue

        amount = booking[7]

        cursor.execute("SELECT COUNT(*) FROM payments")

        result = cursor.fetchone()

        count = result[0]

        payment_id = "PAY" + str(101 + count)

        payment_date = datetime.now().strftime("%d-%m-%Y")

        payment_status = "Paid"

        cursor.execute("""
        INSERT INTO payments
        VALUES(?,?,?,?,?,?)
        """,
        (
            payment_id,
            booking_id,
            payment_method,
            payment_date,
            amount,
            payment_status
        ))

        conn.commit()

        print("\n====================================")
        print("Payment Successful")
        print("Payment ID :", payment_id)
        print("Booking ID :", booking_id)
        print("Amount :", amount)
        print("Payment Method :", payment_method)
        print("Payment Status :", payment_status)
        print("====================================")

        another = input("\nDo you want to make another payment? (Y/N) : ")

        if another == "N" or another == "n":
            break

    conn.close()