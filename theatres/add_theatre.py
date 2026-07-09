from db_connection import get_connection

def add_theatre():

    conn = get_connection()
    cursor = conn.cursor()

    print("\n========== Add Theatre ==========")

    theatre_name = input("Enter Theatre Name : ")
    city = input("Enter City : ")
    total_screens = int(input("Enter Total Screens : "))

    cursor.execute(
        "SELECT * FROM theatres WHERE theatre_name = ?",
        (theatre_name,)
    )

    theatre = cursor.fetchone()

    if theatre is not None:

        print("Theatre Already Exists.")
        conn.close()
        return

    cursor.execute("SELECT theatre_id FROM theatres ORDER BY theatre_id DESC LIMIT 1")
    result = cursor.fetchone()

    if result:
        theatre_id = "THR" + str(int(result[0][3:]) + 1)
    else:
        theatre_id = "THR101"

    cursor.execute("""
    INSERT INTO theatres
    VALUES(?,?,?,?)
    """,
    (
        theatre_id,
        theatre_name,
        city,
        total_screens
    ))

    conn.commit()

    print("\n================================")
    print("Theatre Added Successfully")
    print("Theatre ID :", theatre_id)
    print("================================")

    conn.close()

if __name__ == "__main__":
    add_theatre()

