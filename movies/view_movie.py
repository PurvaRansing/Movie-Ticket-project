from db_connection import get_connection
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def view_movies():

    conn = get_connection()
    cursor = conn.cursor()

    while True:

        console.print(
            Panel.fit(
                "[bold cyan]VIEW MOVIES[/bold cyan]",
                border_style="green"
            )
        )

        console.print("1. View All Movies")
        console.print("2. Sort by Movie Name")
        console.print("3. Sort by Rating")
        console.print("4. Back")

        choice = input("\nEnter Your Choice : ")

        match choice:

            case "1":

                cursor.execute("SELECT * FROM movies")

            case "2":

                cursor.execute(
                    "SELECT * FROM movies ORDER BY movie_name"
                )

            case "3":

                cursor.execute(
                    "SELECT * FROM movies ORDER BY rating DESC"
                )

            case "4":

                conn.close()
                return

            case _:

                console.print("[red]Invalid Choice.[/red]")
                continue

        movies = cursor.fetchall()

        if len(movies) == 0:

            console.print("[red]No Movies Found.[/red]")
            continue

        table = Table(title="Movie Details")

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
        
            
                