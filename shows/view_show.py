from db_connection import get_connection

def view_shows():

    conn = get_connection()
    cursor = conn.cursor()

    while True:

        print("\n========== View Shows ==========")
        print("1. View All Shows")
        print("2. Sort by Show Date")
        print("3. Sort by Show Time")
        print("4. Back")

        choice = input("Enter your choice : ")

        match choice:

            case "1":

                cursor.execute("SELECT * FROM shows")

            case "2":

                cursor.execute(
                    "SELECT * FROM shows ORDER BY show_date"
                )

            case "3":

                cursor.execute(
                    "SELECT * FROM shows ORDER BY show_time"
                )

            case "4":

                conn.close()
                return

            case _:

                print("Invalid Choice.")
                continue

        shows = cursor.fetchall()

        if len(shows) == 0:

            print("\nNo Shows Found.")
            continue

        print("\n===============================================================================")
        print("Show ID\tMovie ID\tTheatre ID\tShow Date\tShow Time")
        print("===============================================================================")

        for show in shows:

            print(
                show[0], "\t",
                show[1], "\t",
                show[2], "\t",
                show[3], "\t",
                show[4]
            )

        print("===============================================================================")

    conn.close()