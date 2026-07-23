from db_connection import get_connection
from rich.console import Console
from rich.panel import Panel

console = Console()


def update_theatre():

    conn = get_connection()
    cursor = conn.cursor()

    while True:

        console.print(
            Panel.fit(
                "[bold cyan]UPDATE THEATRE[/bold cyan]",
                border_style="green"
            )
        )

        theatre_id = input("Enter Theatre ID (0 to Back) : ")

        if theatre_id == "0":
            conn.close()
            return

        cursor.execute(
            "SELECT * FROM theatres WHERE theatre_id = ?",
            (theatre_id,)
        )

        theatre = cursor.fetchone()

        if theatre is None:

            console.print("[bold red]Theatre Not Found.[/bold red]")
            continue

        console.print(f"\n[green]Theatre Name :[/green] {theatre[1]}")
        console.print(f"[green]City :[/green] {theatre[2]}")
        console.print(f"[green]Total Screens :[/green] {theatre[3]}")

        console.print("\n1. Update Theatre Name")
        console.print("2. Update City")
        console.print("3. Update Total Screens")
        console.print("4. Back")

        choice = input("\nEnter Your Choice : ")

        match choice:

            case "1":

                theatre_name = input("Enter New Theatre Name : ").strip()

                cursor.execute(
                    "UPDATE theatres SET theatre_name = ? WHERE theatre_id = ?",
                    (theatre_name, theatre_id)
                )

                conn.commit()

                console.print("[bold green]✓ Theatre Name Updated Successfully[/bold green]")

            case "2":

                city = input("Enter New City : ").strip()

                cursor.execute(
                    "UPDATE theatres SET city = ? WHERE theatre_id = ?",
                    (city, theatre_id)
                )

                conn.commit()

                console.print("[bold green]✓ City Updated Successfully[/bold green]")

            case "3":

                try:

                    total_screens = int(input("Enter New Total Screens : "))

                    if total_screens <= 0:

                        console.print("[bold red]Total Screens Must Be Greater Than 0.[/bold red]")
                        continue

                except:

                    console.print("[bold red]Invalid Number.[/bold red]")
                    continue

                cursor.execute(
                    "UPDATE theatres SET total_screens = ? WHERE theatre_id = ?",
                    (total_screens, theatre_id)
                )

                conn.commit()

                console.print("[bold green]✓ Total Screens Updated Successfully[/bold green]")

            case "4":

                continue

            case _:

                console.print("[bold red]Invalid Choice.[/bold red]")

    conn.close()


if __name__ == "__main__":
    update_theatre()