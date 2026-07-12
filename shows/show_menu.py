from shows.add_show import add_show
from shows.view_show import view_shows
from shows.update_show import update_show
from shows.delete_show import delete_show
from shows.search_show import search_show


def show_menu():

    while True:

        print("\n========== Show Management ==========")
        print("1. Add Show")
        print("2. View Shows")
        print("3. Update Show")
        print("4. Delete Show")
        print("5. Search Show")
        print("6. Return to Admin Menu")

        choice = input("Enter your choice : ")

        match choice:

            case "1":
                add_show()

            case "2":
                view_shows()

            case "3":
                update_show()

            case "4":
                delete_show()

            case "5":
                search_show()

            case "6":
                return

            case _:
                print("Invalid Choice.")