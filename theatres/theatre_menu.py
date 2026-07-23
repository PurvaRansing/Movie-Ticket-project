from theatres.add_theatre import add_theatre
from theatres.delete_theatre import delete_theatre
from theatres.search_theatre import search_theatre
from theatres.update_theatre import update_theatre
from theatres.view_theatre import view_theatre

from rich.console import Console
from rich.panel import Panel

console = Console()


def theatre_menu():

    while True:

        console.print(
            Panel.fit(
                "[bold cyan]🏢 THEATRE MANAGEMENT[/bold cyan]",
                border_style="green"
            )
        )

        console.print("[cyan]1.[/cyan] ➕ Add Theatre")
        console.print("[cyan]2.[/cyan] 🏢 View Theatres")
        console.print("[cyan]3.[/cyan] ✏️ Update Theatre")
        console.print("[cyan]4.[/cyan] 🗑 Delete Theatre")
        console.print("[cyan]5.[/cyan] 🔍 Search Theatre")
        console.print("[cyan]6.[/cyan] 🔙 Return to Admin Menu")

        choice = input("\nEnter Your Choice : ")

        match choice:

            case "1":
                add_theatre()

            case "2":
                view_theatre()

            case "3":
                update_theatre()

            case "4":
                delete_theatre()

            case "5":
                search_theatre()

            case "6":
                console.print("[bold yellow]Returning to Admin Menu...[/bold yellow]")
                return

            case _:
                console.print("[bold red]Invalid Choice! Please Try Again.[/bold red]")


if __name__ == "__main__":
    theatre_menu()