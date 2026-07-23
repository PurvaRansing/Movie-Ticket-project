from movies.add_movie import add_movie
from movies.view_movie import view_movies
from movies.update_movie import update_movie
from movies.delete_movie import delete_movie
from movies.search_movie import search_movie

from rich.console import Console
from rich.panel import Panel

console = Console()


def movie_menu():

    while True:

        console.print(
            Panel.fit(
                "[bold cyan]🎬 MOVIE MANAGEMENT[/bold cyan]",
                border_style="green"
            )
        )

        console.print("[cyan]1.[/cyan] ➕ Add Movie")
        console.print("[cyan]2.[/cyan] 🎥 View Movies")
        console.print("[cyan]3.[/cyan] ✏️ Update Movie")
        console.print("[cyan]4.[/cyan] 🗑 Delete Movie")
        console.print("[cyan]5.[/cyan] 🔍 Search Movie")
        console.print("[cyan]6.[/cyan] 🔙 Back")

        choice = input("\nEnter Your Choice : ")

        match choice:

            case "1":
                add_movie()

            case "2":
                view_movies()

            case "3":
                update_movie()

            case "4":
                delete_movie()

            case "5":
                search_movie()

            case "6":
                console.print("[bold yellow]Returning to Admin Menu...[/bold yellow]")
                return

            case _:
                console.print("[bold red]Invalid Choice! Please Try Again.[/bold red]")
