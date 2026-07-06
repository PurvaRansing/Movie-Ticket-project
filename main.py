from authentication.authentication_menu import authentication_menu

def main():

    while True:

        print("\n===================================")
        print("      CINEFLOW")
        print("Movie Ticket Booking System")
        print("===================================")

        print("1. Authentication")
        print("2. Exit")

        choice = input("Enter your choice : ")

        match choice:

            case "1":
                authentication_menu()

            case "2":
                print("\nThank You!")
                break

            case _:
                print("\nInvalid Choice!")

main()