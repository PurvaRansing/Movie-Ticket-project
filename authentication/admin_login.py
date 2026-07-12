from db_connection import get_connection

def admin_login():

    email = input("Enter Admin Email : ")
    password = input("Enter Password : ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=? AND password=? AND role=?",
        (email, password, "admin")
    )

    admin = cursor.fetchone()

    conn.close()

    if admin:
        print("Admin Login Successful")
        return True
    else:
        print("Invalid Admin Email or Password")
        return False
