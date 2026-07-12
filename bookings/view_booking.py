from db_connection import get_connection

def view_bookings():

    conn = get_connection()
    cursor = conn.cursor()

    while True:

        print("\n========== View Bookings ==========")
        print("1. View All Bookings")
        print("2. Sort by Booking Date")
        print("3. Sort by Amount")
        print("4. Back")

        choice = input("Enter your choice : ")

        match choice:

            case "1":
                cursor.execute("SELECT * FROM bookings")

            case "2":
                cursor.execute(
                    "SELECT * FROM bookings ORDER BY booking_date"
                )

            case "3":
                cursor.execute(
                    "SELECT * FROM bookings ORDER BY total_amount"
                )

            case "4":
                conn.close()
                return

            case _:
                print("Invalid Choice.")
                continue

        bookings = cursor.fetchall()

        if len(bookings) == 0:

            print("No Bookings Found.")
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