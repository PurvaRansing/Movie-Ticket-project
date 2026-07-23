from db_connection import get_connection
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


def cancel_booking():

    conn = get_connection()
    cursor = conn.cursor()

    console.print(
        Panel.fit(
            "[bold red]CANCEL BOOKING[/bold red]",
            border_style="red"
        )
    )

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

    booking = cursor.fetchone()

    if booking is None:

        console.print("[bold red]Booking Not Found.[/bold red]")
        conn.close()
        return

    table = Table(title="Booking Details")

    table.add_column("Booking ID", style="cyan")
    table.add_column("User ID", style="green")
    table.add_column("Movie", style="yellow")
    table.add_column("Seats", style="magenta")
    table.add_column("Amount", style="bright_green")
    table.add_column("Booking Date", style="blue")
    table.add_column("Status", style="red")

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

    if booking[6] == "Cancelled":

        console.print("[bold yellow]This booking is already cancelled.[/bold yellow]")
        conn.close()
        return

    confirm = input("\nAre you sure you want to cancel this booking? (Y/N) : ")

    if confirm.upper() != "Y":

        console.print("[bold yellow]Cancellation Cancelled.[/bold yellow]")
        conn.close()
        return

    cursor.execute(
        """
        UPDATE bookings
        SET status = 'Cancelled'
        WHERE booking_id = ?
        """,
        (booking_id,)
    )

    conn.commit()

    console.print("[bold green]✓ Booking Cancelled Successfully.[/bold green]")

    conn.close()


if __name__ == "__main__":
    cancel_booking()