from db_connection import get_connection
import matplotlib.pyplot as plt

def booking_chart():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT status, COUNT(*)
    FROM bookings
    GROUP BY status
    """)

    data = cursor.fetchall()

    if len(data) == 0:

        print("No Bookings Found.")
        conn.close()
        return

    status = []
    total = []

    for row in data:

        status.append(row[0])
        total.append(row[1])

    plt.pie(total, labels=status, autopct="%1.1f%%")

    plt.title("Booking Status")

    plt.show()

    conn.close()