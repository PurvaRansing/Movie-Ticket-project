# cancel_bookings.py
from db_connection import get_connection

def cancel_booking(customer_id):
    con = get_connection()
    cur = con.cursor()

    print("---- Cancel Booking ----")
    booking_id = int(input("Enter Booking ID: "))

    cur.execute("SELECT show_id, seats_booked FROM bookings WHERE booking_id = %s AND customer_id = %s",
                (booking_id, customer_id))
    booking = cur.fetchone()

    if booking is None:
        print("Booking Not Found!")
        con.close()
        return

    show_id = booking[0]
    seats = booking[1]

    cur.execute("DELETE FROM bookings WHERE booking_id = %s", (booking_id,))
    cur.execute("UPDATE shows SET available_seats = available_seats + %s WHERE show_id = %s",
                (seats, show_id))

    con.commit()
    print("Booking cancelled successfully!")

    con.close()

# Example run
cancel_booking(1)
