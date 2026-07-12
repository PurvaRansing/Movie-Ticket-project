from db_connection import get_connection

def search_movie():

    conn = get_connection()
    cursor = conn.cursor()

    while True:

        print("\n========== Search Movie ==========")
        print("1. Search by Movie ID")
        print("2. Search by Movie Name")
        print("3. Search by Genre")
        print("4. Search by Language")
        print("5. Search by Rating")
        print("6. Search by Ticket Price")
        print("7. Back")

        choice = input("Enter your choice : ")

        match choice:

            case "1":

                movie_id = input("Enter Movie ID : ")

                cursor.execute(
                    "SELECT * FROM movies WHERE movie_id = ?",
                    (movie_id,)
                )

            case "2":

                movie_name = input("Enter Movie Name : ")

                cursor.execute(
                    "SELECT * FROM movies WHERE title = ?",
                    (movie_name,)
                )

            case "3":

                genre = input("Enter Genre : ")

                cursor.execute(
                    "SELECT * FROM movies WHERE genre = ?",
                    (genre,)
                )

            case "4":

                language = input("Enter Language : ")

                cursor.execute(
                    "SELECT * FROM movies WHERE language = ?",
                    (language,)
                )

            case "5":

                rating = float(input("Enter Rating : "))

                cursor.execute(
                    "SELECT * FROM movies WHERE rating >= ?",
                    (rating,)
                )

            case "6":

                price = float(input("Enter Maximum Ticket Price : "))

                cursor.execute(
                    "SELECT * FROM movies WHERE price <= ?",
                    (price,)
                )

            case "7":

                conn.close()
                return

            case _:

                print("Invalid Choice.")
                continue

        movies = cursor.fetchall()

        if len(movies) == 0:

            print("\nNo Movies Found.")
            continue

        print("\n==========================================================================================================")
        print("Movie ID\tMovie Name\tGenre\t\tLanguage\tDuration\tRating\tPrice\tStatus")
        print("==========================================================================================================")

        for movie in movies:

            print(
                movie[0], "\t",
                movie[1], "\t",
                movie[2], "\t",
                movie[3], "\t",
                movie[4], "\t\t",
                movie[5], "\t",
                movie[6], "\t",
                movie[7]
            )

        print("==========================================================================================================")

