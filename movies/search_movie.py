from db_connection import get_connection
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def search_movie():

    conn = get_connection()
    cursor = conn.cursor()

    while True:

        console.print(
            Panel.fit(
                "[bold cyan]SEARCH MOVIE[/bold cyan]",
                border_style="green"
            )
        )

        console.print("1. Search By Movie ID")
        console.print("2. Search By Movie Name")
        console.print("3. Search By Genre")
        console.print("4. Search By Status")
        console.print("5. Back")

        choice = input("\nEnter Your Choice : ")

        match choice:

            case "1":

                movie_id = input("Enter Movie ID : ")

                cursor.execute(
                    "SELECT * FROM movies WHERE movie_id = ?",
                    (movie_id,)
                )

            case "2":

                movie_name = input("Enter Movie Name : ")

                cursor.execute(
                    "SELECT * FROM movies WHERE movie_name LIKE ?",
                    ('%' + movie_name + '%',)
                )

            case "3":

                genre = input("Enter Genre : ")

                cursor.execute(
                    "SELECT * FROM movies WHERE genre LIKE ?",
                    ('%' + genre + '%',)
                )

            case "4":

                status = input("Enter Status (Running/Upcoming/Removed) : ")

                cursor.execute(
                    "SELECT * FROM movies WHERE status = ?",
                    (status,)
                )

            case "5":

                conn.close()
                return

            case _:

                console.print("[red]Invalid Choice.[/red]")
                continue

        movies = cursor.fetchall()

        if len(movies) == 0:

            console.print("[red]No Movie Found.[/red]")
            continue

        table = Table(title="Search Result")

        table.add_column("Movie ID", style="cyan", justify="center")
        table.add_column("Movie Name", style="green")
        table.add_column("Genre", style="yellow")
        table.add_column("Language", style="magenta")
        table.add_column("Duration", justify="center")
        table.add_column("Rating", justify="center")
        table.add_column("Price", justify="right", style="red")
        table.add_column("Status", justify="center", style="blue")

        for movie in movies:

            table.add_row(
                str(movie[0]),
                str(movie[1]),
                str(movie[2]),
                str(movie[3]),
                str(movie[4]) + " Min",
                str(movie[5]),
                "₹" + str(movie[6]),
                str(movie[7])
            )

        console.print(table)

    conn.close()

