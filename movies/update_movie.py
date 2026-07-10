from db_connection import get_connection

def update_movie():

    conn = get_connection()
    cursor = conn.cursor()

    while True:

        print("\n========== Update Movie ==========")
        print("1. Update Movie Name")
        print("2. Update Genre")
        print("3. Update Language")
        print("4. Update Duration")
        print("5. Update Rating")
        print("6. Update Ticket Price")
        print("7. Update Status")
        print("8. Back")

        choice = input("Enter your choice : ")

        if choice == "8":
            conn.close()
            return

        movie_id = input("Enter Movie ID : ")

        cursor.execute("SELECT * FROM movies WHERE movie_id = ?", (movie_id,))
        movie = cursor.fetchone()

        if movie is None:
            print("Movie ID not found.")
            continue

        match choice:

            case "1":

                new_name = input("Enter New Movie Name : ")

                cursor.execute(
                    "UPDATE movies SET movie_name = ? WHERE movie_id = ?",
                    (new_name, movie_id)
                )

                conn.commit()
                print("Movie Name Updated Successfully.")

            case "2":

                print("\nSelect Genre")
                print("1. Action")
                print("2. Comedy")
                print("3. Horror")
                print("4. Romance")
                print("5. Thriller")
                print("6. Drama")

                genre_choice = input("Enter your choice : ")

                match genre_choice:

                    case "1":
                        genre = "Action"
                    case "2":
                        genre = "Comedy"
                    case "3":
                        genre = "Horror"
                    case "4":
                        genre = "Romance"
                    case "5":
                        genre = "Thriller"
                    case "6":
                        genre = "Drama"
                    case _:
                        print("Invalid Choice.")
                        continue

                cursor.execute(
                    "UPDATE movies SET genre = ? WHERE movie_id = ?",
                    (genre, movie_id)
                )

                conn.commit()
                print("Genre Updated Successfully.")

            case "3":

                print("\nSelect Language")
                print("1. Hindi")
                print("2. English")
                print("3. Marathi")
                print("4. Tamil")
                print("5. Telugu")
                print("6. Malayalam")

                language_choice = input("Enter your choice : ")

                match language_choice:

                    case "1":
                        language = "Hindi"
                    case "2":
                        language = "English"
                    case "3":
                        language = "Marathi"
                    case "4":
                        language = "Tamil"
                    case "5":
                        language = "Telugu"
                    case "6":
                        language = "Malayalam"
                    case _:
                        print("Invalid Choice.")
                        continue

                cursor.execute(
                    "UPDATE movies SET language = ? WHERE movie_id = ?",
                    (language, movie_id)
                )

                conn.commit()
                print("Language Updated Successfully.")

            case "4":

                duration = int(input("Enter New Duration : "))

                cursor.execute(
                    "UPDATE movies SET duration = ? WHERE movie_id = ?",
                    (duration, movie_id)
                )

                conn.commit()
                print("Duration Updated Successfully.")

            case "5":

                rating = float(input("Enter New Rating : "))

                if rating < 1 or rating > 10:
                    print("Rating must be between 1 and 10.")
                    continue

                cursor.execute(
                    "UPDATE movies SET rating = ? WHERE movie_id = ?",
                    (rating, movie_id)
                )

                conn.commit()
                print("Rating Updated Successfully.")

            case "6":

                price = float(input("Enter New Ticket Price : "))

                if price <= 0:
                    print("Invalid Price.")
                    continue

                cursor.execute(
                    "UPDATE movies SET price = ? WHERE movie_id = ?",
                    (price, movie_id)
                )

                conn.commit()
                print("Ticket Price Updated Successfully.")

            case "7":

                print("\nSelect Status")
                print("1. Running")
                print("2. Upcoming")
                print("3. Removed")

                status_choice = input("Enter your choice : ")

                match status_choice:

                    case "1":
                        status = "Running"
                    case "2":
                        status = "Upcoming"
                    case "3":
                        status = "Removed"
                    case _:
                        print("Invalid Choice.")
                        continue

                cursor.execute(
                    "UPDATE movies SET status = ? WHERE movie_id = ?",
                    (status, movie_id)
                )

                conn.commit()
                print("Status Updated Successfully.")

            case _:

                print("Invalid Choice.")


        