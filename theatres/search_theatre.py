from db_connection import get_connection
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


def search_theatre():

    conn = get_connection()
    cursor = conn.cursor()

    while True:

        console.print(
            Panel.fit(
                "[bold cyan]SEARCH THEATRE[/bold cyan]",
                border_style="green"
            )
        )

        console.print("1. Search by Theatre ID")
        console.print("2. Search by Theatre Name")
        console.print("3. Search by City")
        console.print("4. Back")

        choice = input("\nEnter Your Choice : ")

        match choice:

            case "1":

                theatre_id = input("Enter Theatre ID : ")

                cursor.execute(
                    "SELECT * FROM theatres WHERE theatre_id = ?",
                    (theatre_id,)
                )

            case "2":

                theatre_name = input("Enter Theatre Name : ")

                cursor.execute(
                    "SELECT * FROM theatres WHERE theatre_name LIKE ?",
                    ('%' + theatre_name + '%',)
                )

            case "3":

                city = input("Enter City : ")

                cursor.execute(
                    "SELECT * FROM theatres WHERE city LIKE ?",
                    ('%' + city + '%',)
                )

            case "4":

                conn.close()
                return

            case _:

                console.print("[bold red]Invalid Choice.[/bold red]")
                continue

        theatres = cursor.fetchall()

        if len(theatres) == 0:

            console.print("[bold red]No Theatre Found.[/bold red]")
            continue

        table = Table(title="Search Result")

        table.add_column("Theatre ID", style="cyan", justify="center")
        table.add_column("Theatre Name", style="green")
        table.add_column("City", style="yellow")
        table.add_column("Total Screens", style="magenta", justify="center")

        for theatre in theatres:

            table.add_row(
                str(theatre[0]),
                str(theatre[1]),
                str(theatre[2]),
                str(theatre[3])
            )

        console.print(table)


if __name__ == "__main__":
    search_theatre()
