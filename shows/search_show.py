from db_connection import get_connection
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


def search_show():

    conn = get_connection()
    cursor = conn.cursor()

    while True:

        console.print(
            Panel.fit(
                "[bold cyan]SEARCH SHOW[/bold cyan]",
                border_style="green"
            )
        )

        console.print("1. Search by Show ID")
        console.print("2. Search by Movie ID")
        console.print("3. Search by Theatre ID")
        console.print("4. Search by Show Date")
        console.print("5. Back")

        choice = input("\nEnter Your Choice : ")

        match choice:

            case "1":

                show_id = input("Enter Show ID : ")

                cursor.execute(
                    "SELECT * FROM shows WHERE show_id = ?",
                    (show_id,)
                )

            case "2":

                movie_id = input("Enter Movie ID : ")

                cursor.execute(
                    "SELECT * FROM shows WHERE movie_id = ?",
                    (movie_id,)
                )

            case "3":

                theatre_id = input("Enter Theatre ID : ")

                cursor.execute(
                    "SELECT * FROM shows WHERE theatre_id = ?",
                    (theatre_id,)
                )

            case "4":

                show_date = input("Enter Show Date (DD-MM-YYYY) : ")

                cursor.execute(
                    "SELECT * FROM shows WHERE show_date = ?",
                    (show_date,)
                )

            case "5":

                conn.close()
                return

            case _:

                console.print("[bold red]Invalid Choice.[/bold red]")
                continue

        shows = cursor.fetchall()

        if len(shows) == 0:

            console.print("[bold red]No Show Found.[/bold red]")
            continue

        table = Table(title="Search Result")

        table.add_column("Show ID", style="cyan", justify="center")
        table.add_column("Movie ID", style="green", justify="center")
        table.add_column("Theatre ID", style="yellow", justify="center")
        table.add_column("Show Date", style="magenta", justify="center")
        table.add_column("Show Time", style="blue", justify="center")

        for show in shows:

            table.add_row(
                str(show[0]),
                str(show[1]),
                str(show[2]),
                str(show[3]),
                str(show[4])
            )

        console.print(table)


if __name__ == "__main__":
    search_show()