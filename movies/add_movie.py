from db_connection import get_connection
from rich.console import Console
from rich.panel import Panel

console = Console()

def add_movie():

    conn = get_connection()
    cursor = conn.cursor()

    console.print(
        Panel.fit(
            "[bold cyan]ADD MOVIE[/bold cyan]",
            border_style="green"
        )
    )

    movie_name = input("Enter Movie Name : ").strip()
    genre = input("Enter Genre : ").strip()
    language = input("Enter Language : ").strip()

    try:
        duration = int(input("Enter Duration (Minutes) : "))
    except:
        console.print("[red]Invalid Duration.[/red]")
        conn.close()
        return

    try:
        rating = float(input("Enter Rating : "))
    except:
        console.print("[red]Invalid Rating.[/red]")
        conn.close()
        return

    try:
        price = float(input("Enter Ticket Price : "))
    except:
        console.print("[red]Invalid Price.[/red]")
        conn.close()
        return

    console.print("\n[bold yellow]Select Movie Status[/bold yellow]")
    console.print("1. Running")
    console.print("2. Upcoming")
    console.print("3. Removed")

    choice = input("Enter Choice : ")

    match choice:

        case "1":
            status = "Running"

        case "2":
            status = "Upcoming"

        case "3":
            status = "Removed"

        case _:
            console.print("[red]Invalid Status.[/red]")
            conn.close()
            return

    cursor.execute(
        "SELECT * FROM movies WHERE movie_name = ?",
        (movie_name,)
    )

    movie = cursor.fetchone()

    if movie:

        console.print("[red]Movie Already Exists.[/red]")
        conn.close()
        return

    cursor.execute("SELECT COUNT(*) FROM movies")

    count = cursor.fetchone()[0]

    movie_id = "MOV" + str(101 + count)

    cursor.execute("""
    INSERT INTO movies
    VALUES(?,?,?,?,?,?,?,?)
    """,
    (
        movie_id,
        movie_name,
        genre,
        language,
        duration,
        rating,
        price,
        status
    ))

    conn.commit()

    console.print("\n[bold green]Movie Added Successfully![/bold green]")
    console.print(f"[cyan]Movie ID :[/cyan] {movie_id}")

    conn.close()

    
            