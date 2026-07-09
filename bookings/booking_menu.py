from book_ticket import book_ticket
from view_booking import view_booking
from cancel_booking import cancel_booking
from search_booking import search_booking

def booking_menu():

    print("\n======================================")
    print("          BOOKING MENU")
    print("=======================================")

    while True:
            
            print("1. Book Ticket\n"
                  "2. View Booking\n"
                  "3. Cancel Booking\n"
                  "4. Search Booking\n"
                  "5. Exit")
        
            choice = int(input("enter your choice:"))
            match choice:
              case 1:
                    book_ticket()
                  
              case 2:
                      view_booking()

              case 3:
                      cancel_booking()

              case 4:
                      search_booking()

              case 5:
                print("Thank you !")
                break
                 
              case _:
                  print("Invalid Choice")

booking_menu()