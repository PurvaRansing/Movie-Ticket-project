from db_connection import get_connection

def register():

    conn = get_connection()
    cursor = conn.cursor()

    print("\n========== Customer Registration ==========")

    user_id = input("Enter User ID : ")
    name = input("Enter Name : ")
    email = input("Enter Email : ")
    mobile = input("Enter Mobile Number : ")
    password = input("Enter Password : ")

    # Check User ID
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()

    if result:
        print("User ID already exists!")
        conn.close()
        return

    # Check Email
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    result = cursor.fetchone()

    if result:
        print("Email already exists!")
        conn.close()
        return

    # Insert Data
    cursor.execute("""
        INSERT INTO users(user_id, name, email, mobile, password, role)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (user_id, name, email, mobile, password, "customer"))

    conn.commit()
    conn.close()

    print("\nRegistration Successful!")