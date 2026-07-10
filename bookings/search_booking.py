from db_connection import get_connection

def search_booking():

    conn = get_connection()
    cursor = conn.cursor()

    while True:

        print("\n========== Search Booking ==========")
        print("1. Search by Booking ID")
        print("2. Search by User ID")
        print("3. Search by Show ID")
        print("4. Back")

        choice = input("Enter your choice : ")

        match choice:

            case "1":

                booking_id = input("Enter Booking ID : ")

                cursor.execute(
                    "SELECT * FROM bookings WHERE booking_id = ?",
                    (booking_id,)
                )

            case "2":

                user_id = input("Enter User ID : ")

                cursor.execute(
                    "SELECT * FROM bookings WHERE user_id = ?",
                    (user_id,)
                )

            case "3":

                show_id = input("Enter Show ID : ")

                cursor.execute(
                    "SELECT * FROM bookings WHERE show_id = ?",
                    (show_id,)
                )

            case "4":

                conn.close()
                return

            case _:

                print("Invalid Choice.")
                continue

        bookings = cursor.fetchall()

        if len(bookings) == 0:

            print("No Booking Found.")
            continue

        print("\n================================================================================================")
        print("Booking ID\tUser ID\tShow ID\tSeat\tAmount\tDate\t\tStatus")
        print("================================================================================================")

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

        print("================================================================================================")

