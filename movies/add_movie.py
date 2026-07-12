from db_connection import get_connection

def add_movie():
    
    print("STEP A")


    conn = get_connection()
    cursor = conn.cursor()

    print("\n========== Add Movie ==========")

    movie_name = input("Enter Movie Name : ")
    genre = input("Enter Genre : ")
    language = input("Enter Language : ")
    duration = int(input("Enter Duration (Minutes) : "))
    rating = float(input("Enter Rating : "))
    price = float(input("Enter Ticket Price : "))

    print("\nSelect Movie Status")
    print("1. Running")
    print("2. Upcoming")
    print("3. Removed")

    choice = input("Enter your choice : ")

    match choice:

        case "1":
            status = "Running"

        case "2":
            status = "Upcoming"

        case "3":
            status = "Removed"

        case _:
            print("Invalid Status.")
            conn.close()
            return

    print("STEP B")


    # Check Duplicate Movie
    cursor.execute(
        "SELECT * FROM movies WHERE title = ?",
        (movie_name,)
    )

    result = cursor.fetchone()

    if result:

        print("\nMovie already exists.")
        conn.close()
        return

    # Generate Movie ID
    cursor.execute("SELECT COUNT(*) FROM movies")

    result = cursor.fetchone()

    count = result[0]
    count = count + 1

    movie_id = "MOV" + str(100 + count)
    
    print("STEP C")

    # Insert Movie
    cursor.execute("""
    INSERT INTO movies
    VALUES(?,?,?,?,?,?,?,?)
    """, (
        movie_id,
        movie_name,
        genre,
        language,
        duration,
        rating,
        price,
        status
    ))

    conn.commit()
    
    print("STEP D")

    print("\nMovie Added Successfully.")
    print("Movie ID :", movie_id)

    conn.close()

    
            