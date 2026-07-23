from db_connection import get_connection
from rich.console import Console
from rich.panel import Panel

console = Console()


def add_show():

    conn = get_connection()
    cursor = conn.cursor()

    console.print(
        Panel.fit(
            "[bold cyan]ADD SHOW[/bold cyan]",
            border_style="green"
        )
    )

    movie_id = input("Enter Movie ID : ").strip()
    theatre_id = input("Enter Theatre ID : ").strip()
    show_date = input("Enter Show Date (DD-MM-YYYY) : ").strip()
    show_time = input("Enter Show Time : ").strip()

    # Check Movie ID
    cursor.execute(
        "SELECT * FROM movies WHERE movie_id = ?",
        (movie_id,)
    )

    movie = cursor.fetchone()

    if movie is None:

        console.print("[bold red]Movie Not Found.[/bold red]")
        conn.close()
        return

    # Check Theatre ID
    cursor.execute(
        "SELECT * FROM theatres WHERE theatre_id = ?",
        (theatre_id,)
    )

    theatre = cursor.fetchone()

    if theatre is None:

        console.print("[bold red]Theatre Not Found.[/bold red]")
        conn.close()
        return

    # Check Duplicate Show
    cursor.execute(
        """
        SELECT * FROM shows
        WHERE movie_id = ?
        AND theatre_id = ?
        AND show_date = ?
        AND show_time = ?
        """,
        (
            movie_id,
            theatre_id,
            show_date,
            show_time
        )
    )

    show = cursor.fetchone()

    if show:

        console.print("[bold red]Show Already Exists.[/bold red]")
        conn.close()
        return

    # Generate Show ID
    cursor.execute("SELECT COUNT(*) FROM shows")

    count = cursor.fetchone()[0]

    show_id = "SHW" + str(101 + count)

    # Insert Show
    cursor.execute("""
    INSERT INTO shows
    VALUES(?,?,?,?,?)
    """,
    (
        show_id,
        movie_id,
        theatre_id,
        show_date,
        show_time
    ))

    conn.commit()

    console.print("\n[bold green]✓ Show Added Successfully[/bold green]")
    console.print(f"[cyan]Show ID :[/cyan] {show_id}")

    conn.close()


if __name__ == "__main__":
    add_show()