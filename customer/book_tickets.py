# book_tickets.py
from db_connection import get_connection
from datetime import datetime

def book_ticket(customer_id):
    con = get_connection()
    cur = con.cursor()

    print("---- Book Ticket ----")
    show_id = int(input("Enter Show ID: "))
    seats = int(input("Enter Number of Seats: "))

    cur.execute("SELECT ticket_price, available_seats FROM shows WHERE show_id = %s", (show_id,))
    show = cur.fetchone()

    if show is None:
        print("Invalid Show ID!")
        con.close()
        return

    ticket_price = show[0]
    available_seats = show[1]

    if seats > available_seats:
        print("Seats Not Available!")
        con.close()
        return

    total_amount = seats * ticket_price
    booking_date = datetime.now().strftime("%d-%m-%Y")

    cur.execute("INSERT INTO bookings(customer_id, show_id, seats_booked, total_amount, booking_date) VALUES (%s, %s, %s, %s, %s)",
                (customer_id, show_id, seats, total_amount, booking_date))

    cur.execute("UPDATE shows SET available_seats = available_seats - %s WHERE show_id = %s",
                (seats, show_id))

    con.commit()
    print("Ticket booked successfully!")

    con.close()

# Example run
book_ticket(1)
