import sqlite3

conn = sqlite3.connect("database/cineflow.db")

cursor = conn.cursor()

# Users Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    user_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    mobile TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL
)
""")

# Movies Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS movies(
    movie_id TEXT PRIMARY KEY,
    movie_name TEXT NOT NULL,
    genre TEXT NOT NULL,
    language TEXT NOT NULL,
    duration INTEGER,
    rating REAL,
    price REAL,
    status TEXT
)
""")

# Theatres Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS theatres(
    theatre_id TEXT PRIMARY KEY,
    theatre_name TEXT NOT NULL,
    city TEXT NOT NULL,
    total_screens INTEGER
)
""")

# Shows Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS shows(
    show_id TEXT PRIMARY KEY,
    movie_id TEXT,
    theatre_id TEXT,
    show_date TEXT,
    show_time TEXT,
    FOREIGN KEY(movie_id) REFERENCES movies(movie_id),
    FOREIGN KEY(theatre_id) REFERENCES theatres(theatre_id)
)
""")

# Bookings Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS bookings(
    booking_id TEXT PRIMARY KEY,
    user_id TEXT,
    show_id TEXT,
    seat_no TEXT,
    total_amount REAL,
    booking_date TEXT,
    status TEXT,
    FOREIGN KEY(user_id) REFERENCES users(user_id),
    FOREIGN KEY(show_id) REFERENCES shows(show_id)
)
""")

# Payments Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS payments(
    payment_id TEXT PRIMARY KEY,
    booking_id TEXT,
    payment_method TEXT,
    amount REAL,
    payment_date TEXT,
    payment_status TEXT,
    FOREIGN KEY(booking_id) REFERENCES bookings(booking_id)
)
""")

conn.commit()

conn.close()

print("Database Created Successfully.")