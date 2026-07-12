from db_connection import get_connection

def delete_show():

    conn = get_connection()
    cursor = conn.cursor()

    while True:

        print("\n========== Delete Show ==========")
        print("1. Delete Show")
        print("2. Back")

        choice = input("Enter your choice : ")

        match choice:

            case "1":

                show_id = input("Enter Show ID : ")

                cursor.execute(
                    "SELECT * FROM shows WHERE show_id = ?",
                    (show_id,)
                )

                show = cursor.fetchone()

                if show is None:

                    print("Show Not Found.")
                    continue

                confirm = input("Are you sure you want to delete this show? (Y/N) : ")

                if confirm == "Y" or confirm == "y":

                    cursor.execute(
                        "DELETE FROM shows WHERE show_id = ?",
                        (show_id,)
                    )

                    conn.commit()

                    print("Show Deleted Successfully.")

                else:

                    print("Deletion Cancelled.")

            case "2":

                conn.close()
                return

            case _:

                print("Invalid Choice.")