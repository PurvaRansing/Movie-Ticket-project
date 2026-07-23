from db_connection import get_connection
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


def search_booking():

    conn = get_connection()
    cursor = conn.cursor()

    while True:

        console.print(
            Panel.fit(
                "[bold cyan]SEARCH BOOKING[/bold cyan]",
                border_style="green"
            )
        )

        console.print("1. Search by Booking ID")
        console.print("2. Search by User ID")
        console.print("3. Search by Show ID")
        console.print("4. Back")

        choice = input("\nEnter Your Choice : ")

        match choice:

            case "1":

                booking_id = input("Enter Booking ID : ")

                cursor.execute("""
                SELECT
                    bookings.booking_id,
                    bookings.user_id,
                    movies.movie_name,
                    bookings.seat_no,
                    bookings.total_amount,
                    bookings.booking_date,
                    bookings.status

                FROM bookings

                JOIN shows
                ON bookings.show_id = shows.show_id

                JOIN movies
                ON shows.movie_id = movies.movie_id

                WHERE bookings.booking_id = ?
                """, (booking_id,))

            case "2":

                user_id = input("Enter User ID : ")

                cursor.execute("""
                SELECT
                    bookings.booking_id,
                    bookings.user_id,
                    movies.movie_name,
                    bookings.seat_no,
                    bookings.total_amount,
                    bookings.booking_date,
                    bookings.status

                FROM bookings

                JOIN shows
                ON bookings.show_id = shows.show_id

                JOIN movies
                ON shows.movie_id = movies.movie_id

                WHERE bookings.user_id = ?
                """, (user_id,))

            case "3":

                show_id = input("Enter Show ID : ")

                cursor.execute("""
                SELECT
                    bookings.booking_id,
                    bookings.user_id,
                    movies.movie_name,
                    bookings.seat_no,
                    bookings.total_amount,
                    bookings.booking_date,
                    bookings.status

                FROM bookings

                JOIN shows
                ON bookings.show_id = shows.show_id

                JOIN movies
                ON shows.movie_id = movies.movie_id

                WHERE bookings.show_id = ?
                """, (show_id,))

            case "4":

                conn.close()
                return

            case _:

                console.print("[bold red]Invalid Choice.[/bold red]")
                continue

        bookings = cursor.fetchall()

        if len(bookings) == 0:

            console.print("[bold red]No Booking Found.[/bold red]")
            continue

        table = Table(title="Booking Search Result")

        table.add_column("Booking ID", style="cyan", justify="center")
        table.add_column("User ID", style="green", justify="center")
        table.add_column("Movie", style="yellow")
        table.add_column("Seats", style="magenta", justify="center")
        table.add_column("Amount", style="bright_green", justify="right")
        table.add_column("Booking Date", style="blue", justify="center")
        table.add_column("Status", style="red", justify="center")

        for booking in bookings:

            table.add_row(
                str(booking[0]),
                str(booking[1]),
                str(booking[2]),
                str(booking[3]),
                "₹" + str(booking[4]),
                str(booking[5]),
                str(booking[6])
            )

        console.print(table)


if __name__ == "__main__":
    search_booking()

