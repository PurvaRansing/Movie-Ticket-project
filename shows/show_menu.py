from db_connection import get_connection

def search_show():

    conn = get_connection()
    cursor = conn.cursor()

    while True:

        print("\n========== Search Show ==========")
        print("1. Search by Show ID")
        print("2. Search by Movie ID")
        print("3. Search by Theatre ID")
        print("4. Search by Show Date")
        print("5. Back")

        choice = input("Enter your choice : ")

        match choice:

            case "1":

                show_id = input("Enter Show ID : ")

                cursor.execute(
                    "SELECT * FROM shows WHERE show_id = ?",
                    (show_id,)
                )

            case "2":

                movie_id = input("Enter Movie ID : ")

                cursor.execute(
                    "SELECT * FROM shows WHERE movie_id = ?",
                    (movie_id,)
                )

            case "3":

                theatre_id = input("Enter Theatre ID : ")

                cursor.execute(
                    "SELECT * FROM shows WHERE theatre_id = ?",
                    (theatre_id,)
                )

            case "4":

                show_date = input("Enter Show Date (DD-MM-YYYY) : ")

                cursor.execute(
                    "SELECT * FROM shows WHERE show_date = ?",
                    (show_date,)
                )

            case "5":

                conn.close()
                return

            case _:

                print("Invalid Choice.")
                continue

        shows = cursor.fetchall()

        if len(shows) == 0:

            print("\nNo Show Found.")
            continue

        print("\n==============================================================================")
        print("Show ID\tMovie ID\tTheatre ID\tShow Date\tShow Time")
        print("==============================================================================")

        for show in shows:

            print(
                show[0], "\t",
                show[1], "\t",
                show[2], "\t",
                show[3], "\t",
                show[4]
            )

        print("==============================================================================")

    conn.close()