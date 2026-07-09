from db_connection import get_connection

def update_theatre():
    conn = get_connection()
    cursor = conn.cursor()

    print("\n----- Update Theatre -----")
    theatre_id = input("Enter the Theatre ID you want to update: ")

    # First, verify if the theatre actually exists
    cursor.execute("SELECT * FROM theatres WHERE theatre_id = ?", (theatre_id,))
    theatre = cursor.fetchone()

    match theatre:
        case None:
            print("Theatre ID not found.")
        case _:
            print(f"\nFound Theatre: {theatre[1]} in {theatre[2]}")
            print("What would you like to update?")
            print("1. Update Theatre Name")
            print("2. Update Theatre City")
            print("3. Back")

            choice = input("Enter your choice: ")

            match choice:
                case "1":
                    new_name = input("Enter new Theatre Name: ")
                    cursor.execute("UPDATE theatres SET theatre_name = ? WHERE theatre_id = ?", (new_name, theatre_id))
                    conn.commit()
                    print("Theatre name updated successfully!")

                case "2":
                    new_city = input("Enter new City: ")
                    cursor.execute("UPDATE theatres SET city = ? WHERE theatre_id = ?", (new_city, theatre_id))
                    conn.commit()
                    print("Theatre city updated successfully!")

                case "3":
                    print("Back to menu.")

                case _:
                    print("Invalid Choice.")

    conn.close()

if __name__ == "__main__":
    update_theatre()