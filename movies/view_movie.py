from db_connection import get_connection

def view_movies():

    conn = get_connection()
    cursor = conn.cursor()

    while True:

        print("\n========== View Movies ==========")
        print("1. View All Movies")
        print("2. View Running Movies")
        print("3. View Upcoming Movies")
        print("4. Sort by Movie Name")
        print("5. Sort by Rating")
        print("6. Sort by Ticket Price")
        print("7. Back")

        choice = input("Enter your choice : ")

        match choice:

            case "1":
                cursor.execute("SELECT * FROM movies")

            case "2":
                cursor.execute("SELECT * FROM movies WHERE status = ?", ("Running",))

            case "3":
                cursor.execute("SELECT * FROM movies WHERE status = ?", ("Upcoming",))

            case "4":
                cursor.execute("SELECT * FROM movies ORDER BY movie_name ASC")

            case "5":
                cursor.execute("SELECT * FROM movies ORDER BY rating DESC")

            case "6":
                cursor.execute("SELECT * FROM movies ORDER BY price ASC")

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

        print("\n==============================================================================================================")
        print("Movie ID\tMovie Name\tGenre\t\tLanguage\tDuration\tRating\tPrice\tStatus")
        print("==============================================================================================================")

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

        print("==============================================================================================================")

        
            
                