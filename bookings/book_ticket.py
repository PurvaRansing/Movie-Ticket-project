from rich.console import Console
from rich.table import Table
from db_connection import get_connection

console = Console()
from datetime import datetime

def book_ticket():

    conn = get_connection()
    cursor = conn.cursor()

    print("\n========== BOOK TICKET ==========")

    # User ID
    user_id = input("Enter User ID : ")

    cursor.execute(
        "SELECT * FROM users WHERE user_id = ?",
        (user_id,)
    )

    user = cursor.fetchone()

    if user is None:

        print("User Not Found.")
        conn.close()
        return

    # Display Available Shows

    cursor.execute("""
    SELECT
        shows.show_id,
        movies.movie_name,
        theatres.theatre_name,
        shows.show_date,
        shows.show_time,
        movies.price

    FROM shows

    JOIN movies
    ON shows.movie_id = movies.movie_id

    JOIN theatres
    ON shows.theatre_id = theatres.theatre_id
    """)

    shows = cursor.fetchall()

    if len(shows) == 0:

        print("No Shows Available.")
        conn.close()
        return

    table = Table(title="Available Shows")

    table.add_column("Show ID", justify="center", style="cyan", no_wrap=True)
    table.add_column("Movie Name", style="green")
    table.add_column("Theatre", style="yellow")
    table.add_column("Show Date", style="magenta")
    table.add_column("Show Time", style="blue")
    table.add_column("Price", justify="right", style="red")

    for show in shows:

        table.add_row(
            str(show[0]),     # Show ID
            str(show[1]),     # Movie Name
            str(show[2]),     # Theatre Name
            str(show[3]),     # Show Date
            str(show[4]),     # Show Time
            f"₹{show[5]}"
        )

    console.print(table)

    show_id = input("\nEnter Show ID : ")

    cursor.execute("""
    SELECT
        shows.show_id,
        movies.movie_name,
        movies.price

    FROM shows

    JOIN movies
    ON shows.movie_id = movies.movie_id

    WHERE shows.show_id = ?
    """,(show_id,))

    show = cursor.fetchone()

    if show is None:

        print("Invalid Show ID.")
        conn.close()
        return

    movie_name = show[1]
    ticket_price = show[2]

    print("\nMovie :", movie_name)
    print("Ticket Price : ₹", ticket_price)

    try:
        total_seats = int(input("\nEnter Number of Seats : "))
    except:
        print("Invalid Input.")
        conn.close()
        return  

    if total_seats <= 0:

        print("Invalid Number of Seats.")
        conn.close()
        return

    # Calculate Total Amount
    total_amount = ticket_price * total_seats

    print("\n==============================")
    print("Movie Name      :", movie_name)
    print("Ticket Price    : ₹", ticket_price)
    print("Total Seats     :", total_seats)
    print("Total Amount    : ₹", total_amount)
    print("==============================")

    seat_no = input("\nEnter Seat Numbers (Example: A1,A2,A3) : ").upper()

    # Generate Booking ID
    cursor.execute("SELECT COUNT(*) FROM bookings")
    count = cursor.fetchone()[0]

    booking_id = "BKG" + str(101 + count)

    booking_date = datetime.now().strftime("%d-%m-%Y")
    status = "Confirmed"

    # Check if seats are already booked for this show

    cursor.execute(
    "SELECT seat_no FROM bookings WHERE show_id = ? AND status = ?",
    (show_id, "Confirmed")
    )

    booked = cursor.fetchall()

    booked_seats = []

    for row in booked:

        seats = row[0].split(",")

        for seat in seats:

            booked_seats.append(seat.strip().upper())

    selected_seats = []

    for seat in seat_no.split(","):

        selected_seats.append(seat.strip().upper())

    for seat in selected_seats:

        if seat in booked_seats:

            print("\nSeat", seat, "is already booked.")
            conn.close()
            return

    cursor.execute("""
    INSERT INTO bookings
    (booking_id,user_id,show_id,seat_no,total_amount,booking_date,status)
    VALUES(?,?,?,?,?,?,?)
    """,
    (
        booking_id,
        user_id,
        show_id,
        seat_no,
        total_amount,
        booking_date,
        status
    ))

    conn.commit()

    print("\n===================================")
    print("Booking Successful")
    print("Booking ID :", booking_id)
    print("Seats      :", seat_no)
    print("Amount     : ₹", total_amount)
    print("===================================")

    conn.close()