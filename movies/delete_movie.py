from db_connection import get_connection

def delete_movie():

    conn = get_connection()
    cursor = conn.cursor()

    while True:

        print("\n========== Delete Movie ==========")
        print("1. Delete Movie by ID")
        print("2. Delete All Removed Movies")
        print("3. Back")

        choice = input("Enter your choice : ")

        match choice:

            case "1":

                movie_id = input("Enter Movie ID : ")

                cursor.execute(
                    "SELECT * FROM movies WHERE movie_id = ?",
                    (movie_id,)
                )

                movie = cursor.fetchone()

                if movie is None:

                    print("Movie ID not found.")
                    continue

                confirm = input("Are you sure you want to delete this movie? (Y/N) : ")

                if confirm == "Y" or confirm == "y":

                    cursor.execute(
                        "DELETE FROM movies WHERE movie_id = ?",
                        (movie_id,)
                    )

                    conn.commit()

                    print("Movie Deleted Successfully.")

                else:

                    print("Delete Cancelled.")

            case "2":

                cursor.execute(
                    "SELECT * FROM movies WHERE status = ?",
                    ("Removed",)
                )

                movies = cursor.fetchall()

                if len(movies) == 0:

                    print("No Removed Movies Found.")
                    continue

                confirm = input("Delete all removed movies? (Y/N) : ")

                if confirm == "Y" or confirm == "y":

                    cursor.execute(
                        "DELETE FROM movies WHERE status = ?",
                        ("Removed",)
                    )

                    conn.commit()

                    print("All Removed Movies Deleted Successfully.")

                else:

                    print("Delete Cancelled.")

            case "3":

                conn.close()
                return

            case _:

                print("Invalid Choice.")
