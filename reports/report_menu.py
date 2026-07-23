from reports.booking_report import booking_report
from reports.movie_report import movie_report
from reports.payment_report import payment_report
from reports.chart_menu import chart_menu

from rich.console import Console
from rich.panel import Panel


console = Console()


def report_menu():

    while True:

        console.print(
            Panel(
                """
1. Booking Report
2. Movie Report
3. Payment Report
4. Charts
5. Back
                """,
                title="Reports Menu",
                border_style="blue"
            )
        )

        choice = input("Enter your choice : ")


        if choice == "1":
            booking_report()

        elif choice == "2":
            movie_report()

        elif choice == "3":
            payment_report()

        elif choice == "4":
            chart_menu()

        elif choice == "5":
            break

        else:
            console.print(
                "[red]Invalid Choice[/red]"
            )