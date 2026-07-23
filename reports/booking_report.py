from db_connection import get_connection

from rich.console import Console
from rich.table import Table
from rich.panel import Panel


console = Console()


def booking_report():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM bookings")

    bookings = cursor.fetchall()


    console.print(
        Panel(
            "Booking Report",
            title="Reports"
        )
    )


    if len(bookings) == 0:

        console.print(
            "[red]No Bookings Found.[/red]"
        )


    else:

        table = Table(
            title="Booking Details"
        )


        table.add_column("Booking ID")
        table.add_column("User ID")
        table.add_column("Show ID")
        table.add_column("Seat No")
        table.add_column("Amount")
        table.add_column("Booking Date")
        table.add_column("Status")


        for booking in bookings:

            table.add_row(
                str(booking[0]),
                str(booking[1]),
                str(booking[2]),
                str(booking[3]),
                str(booking[4]),
                str(booking[5]),
                str(booking[6])
            )


        console.print(table)


        console.print(
            Panel(
                f"Total Bookings : {len(bookings)}",
                title="Summary"
            )
        )


    conn.close()