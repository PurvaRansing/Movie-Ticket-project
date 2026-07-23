from db_connection import get_connection
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


def view_payments():

    conn = get_connection()
    cursor = conn.cursor()

    while True:

        console.print(
            Panel.fit(
                "[bold cyan]VIEW PAYMENTS[/bold cyan]",
                border_style="green"
            )
        )

        print("1. View All Payments")
        print("2. Sort by Payment Date")
        print("3. Sort by Amount")
        print("4. Sort by Payment Method")
        print("5. Back")

        choice = input("\nEnter Your Choice : ")

        if choice == "1":

            cursor.execute("""
            SELECT
                payments.payment_id,
                payments.booking_id,
                movies.movie_name,
                payments.payment_method,
                payments.amount,
                payments.payment_date,
                payments.payment_status

            FROM payments

            JOIN bookings
            ON payments.booking_id = bookings.booking_id

            JOIN shows
            ON bookings.show_id = shows.show_id

            JOIN movies
            ON shows.movie_id = movies.movie_id
            """)

        elif choice == "2":

            cursor.execute("""
            SELECT
                payments.payment_id,
                payments.booking_id,
                movies.movie_name,
                payments.payment_method,
                payments.amount,
                payments.payment_date,
                payments.payment_status

            FROM payments

            JOIN bookings
            ON payments.booking_id = bookings.booking_id

            JOIN shows
            ON bookings.show_id = shows.show_id

            JOIN movies
            ON shows.movie_id = movies.movie_id

            ORDER BY payments.payment_date
            """)

        elif choice == "3":

            cursor.execute("""
            SELECT
                payments.payment_id,
                payments.booking_id,
                movies.movie_name,
                payments.payment_method,
                payments.amount,
                payments.payment_date,
                payments.payment_status

            FROM payments

            JOIN bookings
            ON payments.booking_id = bookings.booking_id

            JOIN shows
            ON bookings.show_id = shows.show_id

            JOIN movies
            ON shows.movie_id = movies.movie_id

            ORDER BY payments.amount
            """)

        elif choice == "4":

            cursor.execute("""
            SELECT
                payments.payment_id,
                payments.booking_id,
                movies.movie_name,
                payments.payment_method,
                payments.amount,
                payments.payment_date,
                payments.payment_status

            FROM payments

            JOIN bookings
            ON payments.booking_id = bookings.booking_id

            JOIN shows
            ON bookings.show_id = shows.show_id

            JOIN movies
            ON shows.movie_id = movies.movie_id

            ORDER BY payments.payment_method
            """)

        elif choice == "5":

            conn.close()
            return

        else:

            console.print("[bold red]Invalid Choice.[/bold red]")
            continue

        payments = cursor.fetchall()

        if len(payments) == 0:

            console.print("[bold yellow]No Payments Found.[/bold yellow]")
            continue

        table = Table(title="Payment Details")

        table.add_column("Payment ID", style="cyan")
        table.add_column("Booking ID", style="green")
        table.add_column("Movie", style="yellow")
        table.add_column("Method", style="magenta")
        table.add_column("Amount", style="bright_green")
        table.add_column("Date", style="blue")
        table.add_column("Status", style="red")

        for payment in payments:

            table.add_row(
                str(payment[0]),
                str(payment[1]),
                str(payment[2]),
                str(payment[3]),
                "₹" + str(payment[4]),
                str(payment[5]),
                str(payment[6])
            )

        console.print(table)


if __name__ == "__main__":
    view_payments()