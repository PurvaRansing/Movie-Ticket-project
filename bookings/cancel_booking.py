from db_connection import get_connection

def cancel_booking():

    conn = get_connection()
    cursor = conn.cursor()

    booking_id = input("Enter Booking ID : ")

    cursor.execute(
        "SELECT * FROM bookings WHERE booking_id = ?",
        (booking_id,)
    )

    if cursor.fetchone() is None:

        print("Booking Not Found.")

    else:

        cursor.execute(
            """
            UPDATE bookings
            SET status = 'Cancelled'
            WHERE booking_id = ?
            """,
            (booking_id,)
        )

        conn.commit()

        print("Booking Cancelled Successfully.")

    conn.close()