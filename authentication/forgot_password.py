from db_connection import get_connection

def forgot_password():

    conn = get_connection()
    cursor = conn.cursor()

    print("\n========== Forgot Password ==========")

    email = input("Enter Email : ")
    mobile = input("Enter Mobile Number : ")

    cursor.execute(
        "SELECT * FROM users WHERE email = ? AND mobile = ?",
        (email, mobile)
    )

    result = cursor.fetchone()

    if result:

        new_password = input("Enter New Password : ")

        cursor.execute(
            "UPDATE users SET password = ? WHERE email = ?",
            (new_password, email)
        )

        conn.commit()

        print("\nPassword Updated Successfully.")
        print("Please login with your new password.")

    else:

        print("\nInvalid Email or Mobile Number.")

    conn.close()