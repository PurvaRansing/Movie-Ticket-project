from db_connection import get_connection
import matplotlib.pyplot as plt

from rich.console import Console
from rich.panel import Panel

console = Console()


def payment_chart():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT payment_method, SUM(amount)
    FROM payments
    GROUP BY payment_method
    """)

    data = cursor.fetchall()

    console.print(
        Panel(
            "Payment Revenue Chart",
            title="Charts",
            border_style="green"
        )
    )

    if len(data) == 0:

        console.print("[red]No Payments Found.[/red]")
        conn.close()
        return

    methods = []
    amounts = []

    for row in data:

        methods.append(row[0])
        amounts.append(row[1])

    plt.figure(figsize=(8, 5))

    plt.bar(methods, amounts)

    plt.title("Revenue by Payment Method")
    plt.xlabel("Payment Method")
    plt.ylabel("Revenue")

    plt.tight_layout()
    plt.show()

    conn.close()