from db_connection import get_connection

def register():

    conn = get_connection()
    cursor = conn.cursor()

    print("\n========== Customer Registration ==========")

    name = input("Enter Name : ")
    email = input("Enter Email : ")
    mobile = input("Enter Mobile Number : ")
    password = input("Enter Password : ")

    # Check Email
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    result = cursor.fetchone()

    if result:
        print("Email already exists.")
        conn.close()
        return

    # Check Mobile Number
    cursor.execute("SELECT * FROM users WHERE mobile = ?", (mobile,))
    result = cursor.fetchone()

    if result:
        print("Mobile Number already exists.")
        conn.close()
        return

    # Generate User ID
    cursor.execute("SELECT COUNT(*) FROM users")
    result = cursor.fetchone()

    count = result[0]
    count = count + 1

    user_id = "USR" + str(100 + count)

    # Insert Data
    cursor.execute("""
    INSERT INTO users(user_id, name, email, mobile, password, role)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (user_id, name, email, mobile, password, "customer"))

    conn.commit()

    print("\nRegistration Successful.")
    print("Your User ID is :", user_id)

    conn.close()