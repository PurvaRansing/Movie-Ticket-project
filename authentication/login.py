from db_connection import get_connection
from admin_menu import admin_menu
from customer_menu import customer_menu


# Admin Login
def admin_login():

    print("\n========== Admin Login ==========")

    email = input("Enter Admin Email : ")
    password = input("Enter Admin Password : ")

    if email == "admin@gmail.com" and password == "admin123":

        print("\nAdmin Login Successful.")
        admin_menu()
        return True

    else:

        print("\nInvalid Admin Email or Password.")
        return False


# Customer Login
def customer_login():

    conn = get_connection()
    cursor = conn.cursor()

    print("\n========== Customer Login ==========")

    email = input("Enter Email : ")
    password = input("Enter Password : ")

    cursor.execute(
        "SELECT * FROM users WHERE email = ? AND password = ?",
        (email, password)
    )

    user = cursor.fetchone()

    conn.close()

    if user:

        print("\nCustomer Login Successful.")
        customer_menu()
        return True

    else:

        print("\nInvalid Email or Password.")
        return False