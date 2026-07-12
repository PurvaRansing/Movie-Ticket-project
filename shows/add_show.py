from db_connection import get_connection

def add_show():

    conn = get_connection()
    cursor = conn.cursor()

    print("\n========== Add Show ==========")

    movie_id = input("Enter Movie ID : ")
    theatre_id = input("Enter Theatre ID : ")
    show_date = input("Enter Show Date (DD-MM-YYYY) : ")
    show_time = input("Enter Show Time : ")

    # Check Movie ID
    cursor.execute(
        "SELECT * FROM movies WHERE movie_id = ?",
        (movie_id,)
    )

    movie = cursor.fetchone()

    if movie is None:

        print("Movie Not Found.")
        conn.close()
        return

    # Check Theatre ID
    cursor.execute(
        "SELECT * FROM theatres WHERE theatre_id = ?",
        (theatre_id,)
    )

    theatre = cursor.fetchone()

    if theatre is None:

        print("Theatre Not Found.")
        conn.close()
        return

    # Generate Show ID
    cursor.execute("SELECT COUNT(*) FROM shows")

    result = cursor.fetchone()

    count = result[0]

    show_id = "SHW" + str(101 + count)

    # Insert Show
    cursor.execute("""
    INSERT INTO shows
    VALUES(?,?,?,?,?)
    """,
    (
        show_id,
        movie_id,
        theatre_id,
        show_date,
        show_time
    ))

    conn.commit()

    print("\n================================")
    print("Show Added Successfully")
    print("Show ID :", show_id)
    print("================================")

    conn.close()