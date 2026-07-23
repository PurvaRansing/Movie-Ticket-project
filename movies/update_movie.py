from db_connection import get_connection
from rich.console import Console
from rich.panel import Panel

console = Console()

def update_movie():

    conn = get_connection()
    cursor = conn.cursor()

    while True:

        console.print(
            Panel.fit(
                "[bold cyan]UPDATE MOVIE[/bold cyan]",
                border_style="green"
            )
        )

        console.print("1. Update Movie Name")
        console.print("2. Update Genre")
        console.print("3. Update Language")
        console.print("4. Update Duration")
        console.print("5. Update Rating")
        console.print("6. Update Ticket Price")
        console.print("7. Update Status")
        console.print("8. Back")

        choice = input("\nEnter Your Choice : ")

        if choice == "8":
            conn.close()
            return

        movie_id = input("Enter Movie ID : ")

        cursor.execute(
            "SELECT * FROM movies WHERE movie_id = ?",
            (movie_id,)
        )

        movie = cursor.fetchone()

        if movie is None:

            console.print("[red]Movie Not Found.[/red]")
            continue

        match choice:

            case "1":

                movie_name = input("Enter New Movie Name : ")

                cursor.execute(
                    "UPDATE movies SET movie_name = ? WHERE movie_id = ?",
                    (movie_name, movie_id)
                )

                conn.commit()

                console.print("[green]Movie Name Updated Successfully.[/green]")

            case "2":

                genre = input("Enter New Genre : ")

                cursor.execute(
                    "UPDATE movies SET genre = ? WHERE movie_id = ?",
                    (genre, movie_id)
                )

                conn.commit()

                console.print("[green]Genre Updated Successfully.[/green]")

            case "3":

                language = input("Enter New Language : ")

                cursor.execute(
                    "UPDATE movies SET language = ? WHERE movie_id = ?",
                    (language, movie_id)
                )

                conn.commit()

                console.print("[green]Language Updated Successfully.[/green]")

            case "4":

                try:

                    duration = int(input("Enter New Duration : "))

                except:

                    console.print("[red]Invalid Duration.[/red]")
                    continue

                cursor.execute(
                    "UPDATE movies SET duration = ? WHERE movie_id = ?",
                    (duration, movie_id)
                )

                conn.commit()

                console.print("[green]Duration Updated Successfully.[/green]")

            case "5":

                try:

                    rating = float(input("Enter New Rating : "))

                except:

                    console.print("[red]Invalid Rating.[/red]")
                    continue

                if rating < 1 or rating > 10:

                    console.print("[red]Rating Must Be Between 1 and 10.[/red]")
                    continue

                cursor.execute(
                    "UPDATE movies SET rating = ? WHERE movie_id = ?",
                    (rating, movie_id)
                )

                conn.commit()

                console.print("[green]Rating Updated Successfully.[/green]")

            case "6":

                try:

                    price = float(input("Enter New Ticket Price : "))

                except:

                    console.print("[red]Invalid Price.[/red]")
                    continue

                if price <= 0:

                    console.print("[red]Price Must Be Greater Than 0.[/red]")
                    continue

                cursor.execute(
                    "UPDATE movies SET price = ? WHERE movie_id = ?",
                    (price, movie_id)
                )

                conn.commit()

                console.print("[green]Ticket Price Updated Successfully.[/green]")

            case "7":

                console.print("\n1. Running")
                console.print("2. Upcoming")
                console.print("3. Removed")

                status_choice = input("Enter Choice : ")

                match status_choice:

                    case "1":
                        status = "Running"

                    case "2":
                        status = "Upcoming"

                    case "3":
                        status = "Removed"

                    case _:

                        console.print("[red]Invalid Status.[/red]")
                        continue

                cursor.execute(
                    "UPDATE movies SET status = ? WHERE movie_id = ?",
                    (status, movie_id)
                )

                conn.commit()

                console.print("[green]Status Updated Successfully.[/green]")

            case _:

                console.print("[red]Invalid Choice.[/red]")


        