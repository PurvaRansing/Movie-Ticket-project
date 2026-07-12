from db_connection import get_connection

def payment_report():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM payments")

    payments = cursor.fetchall()

    print("\n============== Payment Report ==============")

    if len(payments) == 0:

        print("No Payments Found.")

    else:

        print("Payment ID\tBooking ID\tMethod\t\tAmount\t\tDate\t\tStatus")

        for payment in payments:

            print(
                payment[0], "\t",
                payment[1], "\t",
                payment[2], "\t",
                payment[3], "\t",
                payment[4], "\t",
                payment[5]
            )

        print("\nTotal Payments :", len(payments))

    conn.close()