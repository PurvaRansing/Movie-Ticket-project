from db_connection import get_connection
import matplotlib.pyplot as plt

def payment_chart():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT payment_method, SUM(amount)
    FROM payments
    GROUP BY payment_method
    """)

    data = cursor.fetchall()

    if len(data) == 0:

        print("No Payments Found.")
        conn.close()
        return

    methods = []
    amounts = []

    for row in data:

        methods.append(row[0])
        amounts.append(row[1])

    plt.bar(methods, amounts)

    plt.title("Revenue by Payment Method")
    plt.xlabel("Payment Method")
    plt.ylabel("Revenue")

    plt.show()

    conn.close()