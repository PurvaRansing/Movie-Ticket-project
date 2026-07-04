# main.py
import os

def main_menu():
    print("---- Movie Ticket Booking System ----")
    print("1. Admin")
    print("2. Customer")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
       os.system("python.exe admin/admin_menu.py")
    elif choice == "2":
        os.system("python customer/customer_menu.py")
    elif choice == "3":
        print("Thank you for using Movie Ticket System!")
    else:
        print("Invalid choice! Please try again.")
        main_menu()

main_menu()
