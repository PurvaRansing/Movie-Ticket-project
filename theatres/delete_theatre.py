from db_connection import get_connection

def delete_theatre():

    conn = get_connection()
    cursor = conn.cursor()

    while True:

        print("\n========== Delete Theatre ==========")
        print("1. Delete Theatre")
        print("2. Back")

        choice = input("Enter your choice : ")

        match choice:

            case "1":

                theatre_id = input("Enter Theatre ID : ")

                cursor.execute(
                    "SELECT * FROM theatres WHERE theatre_id = ?",
                    (theatre_id,)
                )

                theatre = cursor.fetchone()

                if theatre is None:

                    print("Theatre Not Found.")
                    continue

                confirm = input("Are you sure you want to delete this theatre? (Y/N) : ")

                if confirm == "Y" or confirm == "y":

                    cursor.execute(
                        "DELETE FROM theatres WHERE theatre_id = ?",
                        (theatre_id,)
                    )

                    conn.commit()

                    print("Theatre Deleted Successfully.")

                else:

                    print("Deletion Cancelled.")

            case "2":

                conn.close()
                return

            case _:

                print("Invalid Choice.")

if __name__ == "__main__":
    delete_theatre()