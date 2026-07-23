from db_connection import get_connection

from rich.console import Console
from rich.table import Table
from rich.panel import Panel


console = Console()


def payment_report():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM payments")

    payments = cursor.fetchall()

    console.print(
        Panel(
            "Payment Report",
            title="Reports"
        )
    )

    if len(payments) == 0:

        console.print(
            "[red]No Payments Found.[/red]"
        )

    else:

        table = Table(
            title="Payment Details"
        )

        table.add_column("Payment ID")
        table.add_column("Booking ID")
        table.add_column("Method")
        table.add_column("Amount")
        table.add_column("Date")
        table.add_column("Status")

        for payment in payments:

            table.add_row(
                str(payment[0]),
                str(payment[1]),
                str(payment[2]),
                str(payment[3]),
                str(payment[4]),
                str(payment[5])
            )

        console.print(table)

        console.print(
            Panel(
                f"Total Payments : {len(payments)}",
                title="Summary"
            )
        )

    conn.close()