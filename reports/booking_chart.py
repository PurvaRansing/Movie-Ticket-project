from db_connection import get_connection
import matplotlib.pyplot as plt

from rich.console import Console
from rich.panel import Panel

console = Console()


def booking_chart():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT status, COUNT(*)
    FROM bookings
    GROUP BY status
    """)

    data = cursor.fetchall()

    console.print(
        Panel(
            "Booking Status Chart",
            title="Charts",
            border_style="green"
        )
    )

    if len(data) == 0:

        console.print("[red]No Bookings Found.[/red]")
        conn.close()
        return

    status = []
    total = []

    for row in data:

        status.append(row[0])
        total.append(row[1])

    plt.figure(figsize=(6, 6))

    plt.pie(
        total,
        labels=status,
        autopct="%1.1f%%"
    )

    plt.title("Booking Status")

    plt.tight_layout()
    plt.show()

    conn.close()