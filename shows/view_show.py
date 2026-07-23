from db_connection import get_connection
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


def view_shows():

    conn = get_connection()
    cursor = conn.cursor()

    while True:

        console.print(
            Panel.fit(
                "[bold cyan]VIEW SHOWS[/bold cyan]",
                border_style="green"
            )
        )

        console.print("1. View All Shows")
        console.print("2. Sort by Show Date")
        console.print("3. Sort by Show Time")
        console.print("4. Back")

        choice = input("\nEnter Your Choice : ")

        match choice:

            case "1":

                cursor.execute("""
                SELECT
                    shows.show_id,
                    movies.movie_name,
                    theatres.theatre_name,
                    shows.show_date,
                    shows.show_time,
                    movies.price
                FROM shows
                JOIN movies
                ON shows.movie_id = movies.movie_id
                JOIN theatres
                ON shows.theatre_id = theatres.theatre_id
                """)

            case "2":

                cursor.execute("""
                SELECT
                    shows.show_id,
                    movies.movie_name,
                    theatres.theatre_name,
                    shows.show_date,
                    shows.show_time,
                    movies.price
                FROM shows
                JOIN movies
                ON shows.movie_id = movies.movie_id
                JOIN theatres
                ON shows.theatre_id = theatres.theatre_id
                ORDER BY shows.show_date
                """)

            case "3":

                cursor.execute("""
                SELECT
                    shows.show_id,
                    movies.movie_name,
                    theatres.theatre_name,
                    shows.show_date,
                    shows.show_time,
                    movies.price
                FROM shows
                JOIN movies
                ON shows.movie_id = movies.movie_id
                JOIN theatres
                ON shows.theatre_id = theatres.theatre_id
                ORDER BY shows.show_time
                """)

            case "4":

                conn.close()
                return

            case _:

                console.print("[bold red]Invalid Choice.[/bold red]")
                continue

        shows = cursor.fetchall()

        if len(shows) == 0:

            console.print("[bold red]No Shows Found.[/bold red]")
            continue

        table = Table(title="Show Details")

        table.add_column("Show ID", style="cyan", justify="center")
        table.add_column("Movie Name", style="green")
        table.add_column("Theatre", style="yellow")
        table.add_column("Show Date", style="magenta", justify="center")
        table.add_column("Show Time", style="blue", justify="center")
        table.add_column("Ticket Price", style="bright_green", justify="right")

        for show in shows:

            table.add_row(
                str(show[0]),
                str(show[1]),
                str(show[2]),
                str(show[3]),
                str(show[4]),
                "₹" + str(show[5])
            )

        console.print(table)


if __name__ == "__main__":
    view_shows()