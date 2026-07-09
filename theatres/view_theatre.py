from db_connection import get_connection

def view_theatre():
    conn = get_connection()
    cursor = conn.cursor()

    while True:
        print("\n----- View Theatre Options -----")
        print("1. View All Theatres")
        print("2. Sort by Theatre Name")
        print("3. Sort by City")
        print("4. Back")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                cursor.execute("SELECT * FROM theatres")
                rows = cursor.fetchall()
                
                match rows:
                    case []:
                        print("No theatres found.")
                    case _:
                        for row in rows:
                            print(f"ID: {row[0]} | Name: {row[1]} | City: {row[2]}")

            case "2":
                # ORDER BY theatre_name sorts them alphabetically A-Z
                cursor.execute("SELECT * FROM theatres ORDER BY theatre_name")
                rows = cursor.fetchall()
                
                match rows:
                    case []:
                        print("No theatres found.")
                    case _:
                        for row in rows:
                            print(f"ID: {row[0]} | Name: {row[1]} | City: {row[2]}")

            case "3":
                # ORDER BY city sorts them alphabetically by city name
                cursor.execute("SELECT * FROM theatres ORDER BY city")
                rows = cursor.fetchall()
                
                match rows:
                    case []:
                        print("No theatres found.")
                    case _:
                        for row in rows:
                            print(f"ID: {row[0]} | Name: {row[1]} | City: {row[2]}")

            case "4":
                print("Back")
                break  # Stops this loop to go back to the parent theatre menu cleanly

            case _:
                print("Invalid Choice")

    conn.close()

# Main guard so it doesn't auto-run when imported into theatre_menu.py!
if __name__ == "__main__":
    view_theatre()