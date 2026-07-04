from db_connection import get_connection

conn = get_connection()
cursor = conn.cursor()

# Admin Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS admin1(
    admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
""")

# Customer Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS customer1(
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT,
    phone TEXT,
    password TEXT NOT NULL
)
""")

# Movies Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS movies1(
    movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
    movie_name TEXT NOT NULL,
    language TEXT,
    duration TEXT,
    rating REAL
)
""")

# Shows Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS shows1(
    show_id INTEGER PRIMARY KEY AUTOINCREMENT,
    movie_id INTEGER,
    show_date TEXT,
    show_time TEXT,
    ticket_price REAL,
    available_seats INTEGER,
    FOREIGN KEY(movie_id) REFERENCES movies(movie_id)
)
""")

# Bookings Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS bookings1(
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    show_id INTEGER,
    seats_booked INTEGER,
    total_amount REAL,
    booking_date TEXT,
    FOREIGN KEY(customer_id) REFERENCES customer(customer_id),
    FOREIGN KEY(show_id) REFERENCES shows(show_id)
)
""")

# Default Admin
cursor.execute("SELECT * FROM admin1 WHERE username=?", ("admin",))

if cursor.fetchone() is None:
    cursor.execute(
        "INSERT INTO admin1(username,password) VALUES(?,?)",
        ("admin", "1234")
    )

conn.commit()
conn.close()

print("Database and Tables Created Successfully!")