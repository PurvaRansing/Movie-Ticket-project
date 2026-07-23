from rich.console import Console
from rich.panel import Panel

from bookings.book_ticket import book_ticket
from bookings.view_booking import view_bookings
from bookings.cancel_booking import cancel_booking
from bookings.search_booking import search_booking

console = Console()


def booking_menu():

    while True:

        console.print(
            Panel.fit(
                "[bold cyan]BOOKING MANAGEMENT[/bold cyan]",
                border_style="green"
            )
        )

        console.print("1. Book Ticket")
        console.print("2. View Bookings")
        console.print("3. Cancel Booking")
        console.print("4. Search Booking")
        console.print("5. Back")

        choice = input("\nEnter Your Choice : ")

        match choice:

            case "1":
                book_ticket()

            case "2":
                view_bookings()

            case "3":
                cancel_booking()

            case "4":
                search_booking()

            case "5":
                return

            case _:
                console.print("[bold red]Invalid Choice.[/bold red]")


if __name__ == "__main__":
    booking_menu()