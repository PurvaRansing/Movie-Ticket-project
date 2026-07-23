from db_connection import get_connection
import matplotlib.pyplot as plt

from rich.console import Console
from rich.panel import Panel


console = Console()


def movie_chart():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT movie_name, price FROM movies")
    data = cursor.fetchall()

    console.print(
        Panel(
            "Movie Price Chart",
            title="Charts",
            border_style="green"
        )
    )

    if len(data) == 0:

        console.print("[red]No Movies Found.[/red]")
        conn.close()
        return

    movie_names = []
    prices = []

    for movie in data:

        movie_names.append(movie[0])
        prices.append(movie[1])

    plt.figure(figsize=(8, 5))
    plt.bar(movie_names, prices)

    plt.title("Movie Price Chart")
    plt.xlabel("Movies")
    plt.ylabel("Price")

    plt.tight_layout()
    plt.show()

    conn.close()