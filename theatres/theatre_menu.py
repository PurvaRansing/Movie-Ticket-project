from theatres.add_theatre import add_theatre
from theatres.delete_theatre import delete_theatre
from theatres.search_theatre import search_theatre
from theatres.update_theatre import update_theatre
from theatres.view_theatre import view_theatre


def theatre_menu():

    while True:

        print("\n========== Theatre Management ==========")
        print("1. Add Theatre")
        print("2. View Theatres")
        print("3. Update Theatre")
        print("4. Delete Theatre")
        print("5. Search Theatre")
        print("6. Return to Admin Menu")

        choice = input("Enter your choice : ")

        match choice:

            case "1":
                add_theatre()

            case "2":
                view_theatre()

            case "3":
                update_theatre()

            case "4":
                delete_theatre()

            case "5":
                search_theatre()

            case "6":
                return

            case _:
                print("Invalid Choice.")


if __name__ == "__main__":
    theatre_menu()