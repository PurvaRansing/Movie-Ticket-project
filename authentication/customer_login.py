from db_connection import get_connection

def customer_login():

    email = input("Enter Customer Email : ")
    password = input("Enter Password : ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=? AND password=? AND role=?",
        (email, password, "customer")
    )

    customer = cursor.fetchone()

    conn.close()

    if customer:
        print("Customer Login Successful")
        return True
    else:
        print("Invalid Customer Email or Password")
        return False