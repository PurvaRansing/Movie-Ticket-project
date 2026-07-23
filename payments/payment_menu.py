from payments.make_payment import make_payment
from payments.view_payment import view_payments
from payments.search_payment import search_payment


from rich.console import Console
from rich.panel import Panel

console = Console()


def payment_menu():

    while True:

        console.print(
            Panel.fit(
                "[bold cyan]PAYMENT MANAGEMENT[/bold cyan]",
                border_style="green"
            )
        )

        console.print("1. Make Payment")
        console.print("2. View Payments")
        console.print("3. Search Payment")
        console.print("4. Payment Report")
        console.print("5. Back")

        choice = input("\nEnter Your Choice : ")

        match choice:

            case "1":
                make_payment()

            case "2":
                view_payments()

            case "3":
                search_payment()

            case "4":
                return

            case _:
                console.print("[bold red]Invalid Choice.[/bold red]")


if __name__ == "__main__":
    payment_menu()