from shows.add_show import add_show
from shows.view_show import view_shows
from shows.search_show import search_show
from shows.update_show import update_show
from shows.delete_show import delete_show

from rich.console import Console
from rich.panel import Panel

console = Console()


def show_menu():

    while True:

        console.print(
            Panel.fit(
                "[bold cyan]🎥 SHOW MANAGEMENT[/bold cyan]",
                border_style="green"
            )
        )

        console.print("[cyan]1.[/cyan] ➕ Add Show")
        console.print("[cyan]2.[/cyan] 🎬 View Shows")
        console.print("[cyan]3.[/cyan] ✏️ Update Show")
        console.print("[cyan]4.[/cyan] 🗑 Delete Show")
        console.print("[cyan]5.[/cyan] 🔍 Search Show")
        console.print("[cyan]6.[/cyan] 🔙 Return to Admin Menu")

        choice = input("\nEnter Your Choice : ")

        match choice:

            case "1":
                add_show()

            case "2":
                view_shows()

            case "3":
                update_show()

            case "4":
                delete_show()

            case "5":
                search_show()

            case "6":
                console.print("[bold yellow]Returning to Admin Menu...[/bold yellow]")
                return

            case _:
                console.print("[bold red]Invalid Choice! Please Try Again.[/bold red]")


if __name__ == "__main__":
    show_menu()