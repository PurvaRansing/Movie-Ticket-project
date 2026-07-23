from db_connection import get_connection
from rich.console import Console
from rich.panel import Panel

console = Console()


def delete_theatre():

    conn = get_connection()
    cursor = conn.cursor()

    while True:

        console.print(
            Panel.fit(
                "[bold red]DELETE THEATRE[/bold red]",
                border_style="red"
            )
        )

        console.print("1. Delete Theatre")
        console.print("2. Back")

        choice = input("\nEnter Your Choice : ")

        match choice:

            case "1":

                theatre_id = input("Enter Theatre ID : ")

                cursor.execute(
                    "SELECT * FROM theatres WHERE theatre_id = ?",
                    (theatre_id,)
                )

                theatre = cursor.fetchone()

                if theatre is None:

                    console.print("[bold red]Theatre Not Found.[/bold red]")
                    continue

                console.print("\n[bold yellow]Theatre Details[/bold yellow]")
                console.print(f"Theatre ID      : {theatre[0]}")
                console.print(f"Theatre Name    : {theatre[1]}")
                console.print(f"City            : {theatre[2]}")
                console.print(f"Total Screens   : {theatre[3]}")

                confirm = input("\nAre you sure you want to delete this theatre? (Y/N) : ")

                if confirm.upper() == "Y":

                    cursor.execute(
                        "DELETE FROM theatres WHERE theatre_id = ?",
                        (theatre_id,)
                    )

                    conn.commit()

                    console.print("[bold green]✓ Theatre Deleted Successfully[/bold green]")

                else:

                    console.print("[bold yellow]Deletion Cancelled.[/bold yellow]")

            case "2":

                conn.close()
                return

            case _:

                console.print("[bold red]Invalid Choice.[/bold red]")


if __name__ == "__main__":
    delete_theatre()