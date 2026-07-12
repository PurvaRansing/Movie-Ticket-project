from db_connection import get_connection

def movie_report():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM movies")

    movies = cursor.fetchall()

    print("\n============== Movie Report ==============")

    if len(movies) == 0:

        print("No Movies Found.")

    else:

        print("Movie ID\tMovie Name\tGenre\tLanguage\tPrice\tStatus")

        for movie in movies:

            print(
                movie[0], "\t",
                movie[1], "\t",
                movie[2], "\t",
                movie[3], "\t",
                movie[6], "\t",
                movie[7]
            )

        print("\nTotal Movies :", len(movies))

    conn.close()