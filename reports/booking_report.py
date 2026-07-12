from db_connection import get_connection

def booking_report():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM bookings")

    bookings = cursor.fetchall()

    print("\n============== Booking Report ==============")

    if len(bookings) == 0:

        print("No Bookings Found.")

    else:

        print("Booking ID\tUser ID\t\tShow ID\t\tSeat No\t\tAmount\t\tBooking Date\tStatus")

        for booking in bookings:

            print(
                booking[0], "\t",
                booking[1], "\t",
                booking[2], "\t",
                booking[3], "\t",
                booking[4], "\t",
                booking[5], "\t",
                booking[6]
            )

        print("\nTotal Bookings :", len(bookings))

    conn.close()