from db_connection import get_connection

def search_theatre():
    conn = get_connection()
    cursor = conn.cursor()

    while True:
        print("\n=========Search Theatre=========")
        print("1. Search by Theatre ID")
        print("2. Search by Theatre Name")
        print("3. Search by City")
        print("4. Back")

        choice = input("Enter your choice: ")

        match choice:

            case "1":
                theatre_id = input("Enter Theatre ID: ")
                cursor.execute("SELECT * FROM theatres WHERE theatre_id = ?", (theatre_id,))
                data = cursor.fetchall()

                if data:
                    print(data)
                else:
                    print("Theatre ID not found.")

            case "2":
                name = input("Enter Theatre Name: ")
                cursor.execute("SELECT * FROM theatres WHERE theatre_name = ?", (name,))
                data = cursor.fetchall()

                if data:
                    print(data)
                else:
                    print("Theatre Name not found.")

            case "3":
                city = input("Enter City: ")
                cursor.execute("SELECT * FROM theatres WHERE city = ?", (city,))
                data = cursor.fetchall()

                if data:
                    print(data)
                else:
                    print("City not found.")

            case "4":
                print("Back")
                break

            case _:
                print("Invalid Choice")

    conn.close()
    
if __name__ == "__main__":
    search_theatre()
