from db_connection import get_connection
from rich.console import Console
from rich.panel import Panel

console = Console()


def delete_show():

    conn = get_connection()
    cursor = conn.cursor()

    while True:

        console.print(
            Panel.fit(
                "[bold red]DELETE SHOW[/bold red]",
                border_style="red"
            )
        )

        console.print("1. Delete Show")
        console.print("2. Back")

        choice = input("\nEnter Your Choice : ")

        match choice:

            case "1":

                show_id = input("Enter Show ID : ")

                cursor.execute(
                    """
                    SELECT
                        shows.show_id,
                        movies.movie_name,
                        theatres.theatre_name,
                        shows.show_date,
                        shows.show_time
                    FROM shows
                    JOIN movies
                    ON shows.movie_id = movies.movie_id
                    JOIN theatres
                    ON shows.theatre_id = theatres.theatre_id
                    WHERE shows.show_id = ?
                    """,
                    (show_id,)
                )

                show = cursor.fetchone()

                if show is None:

                    console.print("[bold red]Show Not Found.[/bold red]")
                    continue

                console.print("\n[bold yellow]Show Details[/bold yellow]")
                console.print(f"Show ID      : {show[0]}")
                console.print(f"Movie        : {show[1]}")
                console.print(f"Theatre      : {show[2]}")
                console.print(f"Show Date    : {show[3]}")
                console.print(f"Show Time    : {show[4]}")

                confirm = input("\nAre you sure you want to delete this show? (Y/N) : ")

                if confirm.upper() == "Y":

                    cursor.execute(
                        "DELETE FROM shows WHERE show_id = ?",
                        (show_id,)
                    )

                    conn.commit()

                    console.print("[bold green]✓ Show Deleted Successfully[/bold green]")

                else:

                    console.print("[bold yellow]Deletion Cancelled.[/bold yellow]")

            case "2":

                conn.close()
                return

            case _:

                console.print("[bold red]Invalid Choice.[/bold red]")


if __name__ == "__main__":
    delete_show()