from db_connection import get_connection
from rich.console import Console
from rich.panel import Panel

console = Console()


def update_show():

    conn = get_connection()
    cursor = conn.cursor()

    while True:

        console.print(
            Panel.fit(
                "[bold cyan]UPDATE SHOW[/bold cyan]",
                border_style="green"
            )
        )

        console.print("1. Update Show Date")
        console.print("2. Update Show Time")
        console.print("3. Update Theatre")
        console.print("4. Back")

        choice = input("\nEnter Your Choice : ")

        if choice == "4":
            conn.close()
            return

        show_id = input("Enter Show ID : ")

        cursor.execute(
            "SELECT * FROM shows WHERE show_id = ?",
            (show_id,)
        )

        show = cursor.fetchone()

        if show is None:

            console.print("[bold red]Show Not Found.[/bold red]")
            continue

        match choice:

            case "1":

                show_date = input("Enter New Show Date (DD-MM-YYYY) : ")

                cursor.execute(
                    """
                    UPDATE shows
                    SET show_date = ?
                    WHERE show_id = ?
                    """,
                    (show_date, show_id)
                )

                conn.commit()

                console.print("[bold green]✓ Show Date Updated Successfully[/bold green]")

            case "2":

                show_time = input("Enter New Show Time : ")

                cursor.execute(
                    """
                    UPDATE shows
                    SET show_time = ?
                    WHERE show_id = ?
                    """,
                    (show_time, show_id)
                )

                conn.commit()

                console.print("[bold green]✓ Show Time Updated Successfully[/bold green]")

            case "3":

                theatre_id = input("Enter New Theatre ID : ")

                cursor.execute(
                    "SELECT * FROM theatres WHERE theatre_id = ?",
                    (theatre_id,)
                )

                theatre = cursor.fetchone()

                if theatre is None:

                    console.print("[bold red]Theatre Not Found.[/bold red]")
                    continue

                cursor.execute(
                    """
                    UPDATE shows
                    SET theatre_id = ?
                    WHERE show_id = ?
                    """,
                    (theatre_id, show_id)
                )

                conn.commit()

                console.print("[bold green]✓ Theatre Updated Successfully[/bold green]")

            case _:

                console.print("[bold red]Invalid Choice.[/bold red]")


if __name__ == "__main__":
    update_show()