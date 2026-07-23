from db_connection import get_connection
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


def view_theatre():

    conn = get_connection()
    cursor = conn.cursor()

    while True:

        console.print(
            Panel.fit(
                "[bold cyan]VIEW THEATRES[/bold cyan]",
                border_style="green"
            )
        )

        console.print("1. View All Theatres")
        console.print("2. Sort by Theatre Name")
        console.print("3. Sort by City")
        console.print("4. Back")

        choice = input("\nEnter Your Choice : ")

        match choice:

            case "1":

                cursor.execute("SELECT * FROM theatres")

            case "2":

                cursor.execute(
                    "SELECT * FROM theatres ORDER BY theatre_name"
                )

            case "3":

                cursor.execute(
                    "SELECT * FROM theatres ORDER BY city"
                )

            case "4":

                conn.close()
                return

            case _:

                console.print("[bold red]Invalid Choice![/bold red]")
                continue

        theatres = cursor.fetchall()

        if len(theatres) == 0:

            console.print("[bold red]No Theatres Found.[/bold red]")
            continue

        table = Table(title="Theatre Details")

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
    view_theatre()