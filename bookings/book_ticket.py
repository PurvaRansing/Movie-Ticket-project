from db_connection import get_connection
from datetime import datetime


def  book_ticket():

    conn = get_connection()
    cursor = conn.cursor()
    print("\n========== BOOKING MENU ==========")

    user_id = (input("enter user id : "))
    show_id = (input("enter show id :"))
    seat_no = (input("enter seat id :"))
    total_amount = (input("enter total amount"))


    cursor.execute("SELECT * FROM  users WHERE  user_id = ?",(user_id,))
    user = cursor.fetchone()

    if user is None:
        print("user  Not Found.")
        conn.close()
        return
    
    cursor.execute("SELECT * FROM shows WHERE show_id = ?",(show_id,))
    show = cursor.fetchone()

    if show is None:
        print("show  Not Found.")
        conn.close()
        return
    
    cursor.execute("select count(*) from bookings ")
    count = cursor.fetchone()[0]

    booking_id = "BKG" + str(101 + count)

#DATE AND TIME 
    booking_date = datetime.now().strftime("%d/%m/9%y")
    status = "Confirmed"

    #INSERT QUERY
    cursor.execute("""
INSERT INTO bookings
(booking_id, user_id, show_id, seat_no, total_amount, booking_date, status)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", (
    booking_id,
    user_id,
    show_id,
    seat_no,
    total_amount,
    booking_date,
    status
))
    conn.commit()
    print("\nBooking Successful!")
    print("Booking ID:", booking_id)
    conn.close()