from db_connection import get_connection
import matplotlib.pyplot as plt


def movie_chart():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT movie_name, price FROM movies")

    data = cursor.fetchall()

    if len(data) == 0:

        print("No Movies Found.")
        conn.close()
        return

    movie_names = []
    prices = []

    for movie in data:

        movie_names.append(movie[0])
        prices.append(movie[1])

    plt.bar(movie_names, prices)

    plt.title("Movie Price Chart")
    plt.xlabel("Movies")
    plt.ylabel("Price")

    plt.show()

    conn.close()