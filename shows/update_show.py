from db_connection import get_connection

def update_show():

    conn = get_connection()
    cursor = conn.cursor()

    while True:

        print("\n========== Update Show ==========")
        print("1. Update Show Date")
        print("2. Update Show Time")
        print("3. Update Theatre")
        print("4. Back")

        choice = input("Enter your choice : ")

        if choice == "4":
            conn.close()
            return

        show_id = input("Enter Show ID : ")

        cursor.execute(
            "SELECT * FROM shows WHERE show_id = ?",
            (show_id,)
        )

        show = cursor.fetchone()

        if show is None:

            print("Show Not Found.")
            continue

        match choice:

            case "1":

                show_date = input("Enter New Show Date (DD-MM-YYYY) : ")

                cursor.execute(
                    """
                    UPDATE shows
                    SET show_date = ?
                    WHERE show_id = ?
                    """,
                    (show_date, show_id)
                )

                conn.commit()

                print("Show Date Updated Successfully.")

            case "2":

                show_time = input("Enter New Show Time : ")

                cursor.execute(
                    """
                    UPDATE shows
                    SET show_time = ?
                    WHERE show_id = ?
                    """,
                    (show_time, show_id)
                )

                conn.commit()

                print("Show Time Updated Successfully.")

            case "3":

                theatre_id = input("Enter New Theatre ID : ")

                cursor.execute(
                    "SELECT * FROM theatres WHERE theatre_id = ?",
                    (theatre_id,)
                )

                theatre = cursor.fetchone()

                if theatre is None:

                    print("Theatre Not Found.")
                    continue

                cursor.execute(
                    """
                    UPDATE shows
                    SET theatre_id = ?
                    WHERE show_id = ?
                    """,
                    (theatre_id, show_id)
                )

                conn.commit()

                print("Theatre Updated Successfully.")

            case _:

                print("Invalid Choice.")