from db_connection import get_connection

def login():

    conn = get_connection()
    cursor = conn.cursor()

    print("\n========== Login ==========")

    email = input("Enter Email : ")
    password = input("Enter Password : ")

    cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))

    result = cursor.fetchone()

    if result:

        print("\nLogin Successful!")

        if result[5] == "admin":
            print("Welcome Admin")
            # admin_dashboard()

        elif result[5] == "customer":
            print("Welcome Customer")
            # customer_dashboard()

    else:
        print("\nInvalid Email or Password!")

    conn.close()