from db_connection import get_connection
from rich.console import Console
from rich.panel import Panel

console = Console()


def add_theatre():

    conn = get_connection()
    cursor = conn.cursor()

    console.print(
        Panel.fit(
            "[bold cyan]ADD THEATRE[/bold cyan]",
            border_style="green"
        )
    )

    theatre_name = input("Enter Theatre Name : ").strip()
    city = input("Enter City : ").strip()

    try:
        total_screens = int(input("Enter Total Screens : "))

        if total_screens <= 0:
            console.print("[bold red]Total Screens must be greater than 0.[/bold red]")
            conn.close()
            return

    except:

        console.print("[bold red]Invalid Number of Screens.[/bold red]")
        conn.close()
        return

    cursor.execute(
        "SELECT * FROM theatres WHERE theatre_name = ?",
        (theatre_name,)
    )

    theatre = cursor.fetchone()

    if theatre:

        console.print("[bold red]Theatre Already Exists.[/bold red]")
        conn.close()
        return

    cursor.execute("SELECT COUNT(*) FROM theatres")

    count = cursor.fetchone()[0]

    theatre_id = "THR" + str(101 + count)

    cursor.execute("""
    INSERT INTO theatres
    VALUES(?,?,?,?)
    """,
    (
        theatre_id,
        theatre_name,
        city,
        total_screens
    ))

    conn.commit()

    console.print("\n[bold green]✓ Theatre Added Successfully[/bold green]")
    console.print(f"[cyan]Theatre ID :[/cyan] {theatre_id}")

    conn.close()


if __name__ == "__main__":
    add_theatre()

