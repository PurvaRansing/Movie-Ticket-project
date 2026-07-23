from reports.movie_chart import movie_chart
from reports.booking_chart import booking_chart
from reports.payment_chart import payment_chart

from rich.console import Console
from rich.panel import Panel


console = Console()


def chart_menu():

    while True:

        console.print(
            Panel(
                """
1. Movie Chart
2. Booking Chart
3. Payment Chart
4. Return to Admin Menu
                """,
                title="Charts",
                border_style="cyan"
            )
        )

        choice = input("Enter your choice : ")

        match choice:

            case "1":
                movie_chart()

            case "2":
                booking_chart()

            case "3":
                payment_chart()

            case "4":
                return

            case _:
                console.print("[red]Invalid Choice.[/red]")