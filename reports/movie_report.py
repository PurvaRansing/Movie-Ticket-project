from db_connection import get_connection

from rich.console import Console
from rich.table import Table
from rich.panel import Panel


console = Console()


def movie_report():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM movies")

    movies = cursor.fetchall()


    console.print(
        Panel(
            "Movie Report",
            title="Reports"
        )
    )


    if len(movies) == 0:

        console.print(
            "[red]No Movies Found.[/red]"
        )


    else:

        table = Table(
            title="Movie Details"
        )


        table.add_column("Movie ID")
        table.add_column("Movie Name")
        table.add_column("Genre")
        table.add_column("Language")
        table.add_column("Price")
        table.add_column("Status")


        for movie in movies:

            table.add_row(
                str(movie[0]),
                str(movie[1]),
                str(movie[2]),
                str(movie[3]),
                str(movie[6]),
                str(movie[7])
            )


        console.print(table)


        console.print(
            Panel(
                f"Total Movies : {len(movies)}",
                title="Summary"
            )
        )


    conn.close()