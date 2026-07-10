from movies.add_movie import add_movie
from movies.view_movie import view_movies
from movies.update_movie import update_movie
from movies.delete_movie import delete_movie
from movies.search_movie import search_movie


def movie_menu():

    while True:

        print("\n========== Movie Management ==========")
        print("1. Add Movie")
        print("2. View Movies")
        print("3. Update Movie")
        print("4. Delete Movie")
        print("5. Search Movie")
        print("6. Back")

        choice = input("Enter your choice : ")

        match choice:

            case "1":
                add_movie()

            case "2":
                view_movies()

            case "3":
                update_movie()

            case "4":
                delete_movie()

            case "5":
                search_movie()

            case "6":
                return

            case _:
                print("Invalid Choice.")
