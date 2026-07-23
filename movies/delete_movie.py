from db_connection import get_connection
from rich.console import Console
from rich.panel import Panel

console = Console()

def delete_movie():

    conn = get_connection()
    cursor = conn.cursor()

    while True:

        console.print(
            Panel.fit(
                "[bold red]DELETE MOVIE[/bold red]",
                border_style="red"
            )
        )

        movie_id = input("Enter Movie ID (0 to Back): ")

        if movie_id == "0":
            conn.close()
            return

        cursor.execute(
            "SELECT * FROM movies WHERE movie_id = ?",
            (movie_id,)
        )

        movie = cursor.fetchone()

        if movie is None:

            console.print("[red]Movie Not Found.[/red]")
            continue

        console.print("\nMovie Details")
        console.print(f"Movie ID     : {movie[0]}")
        console.print(f"Movie Name   : {movie[1]}")
        console.print(f"Genre        : {movie[2]}")
        console.print(f"Language     : {movie[3]}")
        console.print(f"Duration     : {movie[4]} Minutes")
        console.print(f"Rating       : {movie[5]}")
        console.print(f"Price        : ₹{movie[6]}")
        console.print(f"Status       : {movie[7]}")

        choice = input("\nAre you sure you want to delete this movie? (Y/N): ")

        if choice.upper() == "Y":

            cursor.execute(
                "DELETE FROM movies WHERE movie_id = ?",
                (movie_id,)
            )

            conn.commit()

            console.print("[bold green]Movie Deleted Successfully.[/bold green]")

        else:

            console.print("[yellow]Delete Cancelled.[/yellow]")
