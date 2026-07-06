import sqlite3

def get_connection():
    conn = sqlite3.connect("database/cineflow.db")
    return conn
