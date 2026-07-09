from db_connection import get_connection

def view_booking():
     
     conn = get_connection()
     cursor = conn.cursor()

     print("\n==========  VIEW BOOKING  ==========")

     booking_id = input("enter your booking id :")

     cursor.execute ("SELECT * FROM bookings WHERE booking_id=?",(booking_id,))

     booking =cursor.fetchone()

     if booking:
          print("Booking ID :",booking[0])
          print("User ID :",booking[1])
          print("Show ID :",booking[2])
          print("Seat NO :",booking[3])
          print("Total-Amount :",booking[4])
          print("Booking Date :",booking[5])
          print("Status :",booking[6])
     else:
          print("Booking Not Found!")
    

     conn.close()