from db_connection import get_connection
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


def view_bookings():

    conn = get_connection()
    cursor = conn.cursor()

    while True:

        console.print(
            Panel.fit(
                "[bold cyan]VIEW BOOKINGS[/bold cyan]",
                border_style="green"
            )
        )

        console.print("1. View All Bookings")
        console.print("2. Sort by Booking Date")
        console.print("3. Sort by Amount")
        console.print("4. Back")

        choice = input("\nEnter Your Choice : ")

        match choice:

            case "1":

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
                """)

            case "2":

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

                ORDER BY bookings.booking_date
                """)

            case "3":

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

                ORDER BY bookings.total_amount
                """)

            case "4":

                conn.close()
                return

            case _:

                console.print("[bold red]Invalid Choice.[/bold red]")
                continue

        bookings = cursor.fetchall()

        if len(bookings) == 0:

            console.print("[bold red]No Bookings Found.[/bold red]")
            continue

        table = Table(title="Booking Details")

        table.add_column("Booking ID", style="cyan", justify="center")
        table.add_column("User ID", style="green", justify="center")
        table.add_column("Movie", style="yellow")
        table.add_column("Seats", style="magenta")
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
    view_bookings()