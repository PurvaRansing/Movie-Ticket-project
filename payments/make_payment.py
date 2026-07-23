from db_connection import get_connection
from datetime import datetime

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from utils.generate_qr import generate_qr
from utils.generate_pdf import generate_pdf
from utils.send_email import send_email

console = Console()


def make_payment():

    conn = get_connection()
    cursor = conn.cursor()

    console.print(
        Panel.fit(
            "[bold cyan]MAKE PAYMENT[/bold cyan]",
            border_style="green"
        )
    )

    booking_id = input("Enter Booking ID : ")

    cursor.execute("""
    SELECT
        bookings.booking_id,
        bookings.user_id,
        bookings.show_id,
        bookings.seat_no,
        bookings.total_amount,
        bookings.booking_date,
        bookings.status,
        users.email,
        movies.movie_name,
        theatres.theatre_name,
        shows.show_date,
        shows.show_time

    FROM bookings

    JOIN users
    ON bookings.user_id = users.user_id

    JOIN shows
    ON bookings.show_id = shows.show_id

    JOIN movies
    ON shows.movie_id = movies.movie_id

    JOIN theatres
    ON shows.theatre_id = theatres.theatre_id

    WHERE bookings.booking_id = ?
    """,(booking_id,))

    booking = cursor.fetchone()

    if booking is None:

        console.print("[bold red]Booking Not Found.[/bold red]")
        conn.close()
        return

    if booking[6] == "Cancelled":

        console.print("[bold red]This Booking is Cancelled.[/bold red]")
        conn.close()
        return

    cursor.execute(
        "SELECT * FROM payments WHERE booking_id = ?",
        (booking_id,)
    )

    payment = cursor.fetchone()

    if payment is not None:

        console.print("[bold yellow]Payment Already Completed.[/bold yellow]")
        conn.close()
        return

    table = Table(title="Booking Details")

    table.add_column("Booking ID")
    table.add_column("Movie")
    table.add_column("Theatre")
    table.add_column("Seats")
    table.add_column("Amount")

    table.add_row(
        booking[0],
        booking[8],
        booking[9],
        booking[3],
        "₹" + str(booking[4])
    )

    console.print(table)

    print("\nPayment Method")
    print("1. Cash")
    print("2. UPI")
    print("3. Card")

    choice = input("Enter Choice : ")

    match choice:

        case "1":
            payment_method = "Cash"

        case "2":
            payment_method = "UPI"

        case "3":
            payment_method = "Card"

        case _:
            console.print("[bold red]Invalid Choice.[/bold red]")
            conn.close()
            return

    confirm = input("\nConfirm Payment (Y/N) : ")

    if confirm.upper() != "Y":

        console.print("[bold yellow]Payment Cancelled.[/bold yellow]")
        conn.close()
        return

    cursor.execute("SELECT COUNT(*) FROM payments")

    count = cursor.fetchone()[0]

    payment_id = "PAY" + str(101 + count)

    payment_date = datetime.now().strftime("%d-%m-%Y")

    payment_status = "Paid"

    amount = booking[4]

        # Generate QR Code

    qr_path = generate_qr(
        booking_id=booking[0],
        payment_id=payment_id,
        movie_name=booking[8],
        seats=booking[3],
        amount=amount
    )

    # Generate PDF Receipt

    pdf_path = generate_pdf(
        booking_id=booking[0],
        payment_id=payment_id,
        user_id=booking[1],
        movie_name=booking[8],
        theatre_name=booking[9],
        show_date=booking[10],
        show_time=booking[11],
        seats=booking[3],
        amount=amount,
        payment_method=payment_method,
        payment_date=payment_date,
        qr_path=qr_path
    )

    # Save Payment Details
    print("PDF Path =", pdf_path)
    cursor.execute("""
    INSERT INTO payments
    (
        payment_id,
        booking_id,
        payment_method,
        amount,
        payment_date,
        payment_status,
        razorpay_payment_id,
        receipt_path
    )
    VALUES(?,?,?,?,?,?,?,?)
    """,
    (
        payment_id,
        booking_id,
        payment_method,
        amount,
        payment_date,
        payment_status,
        "TEST_PAYMENT_ID",
        pdf_path
    ))

    conn.commit()

    # Send Receipt Email

    receiver_email = booking[7]

    send_email(
        receiver_email,
        pdf_path
    )

    # Success Message

    console.print(
        Panel.fit(
            "[bold green]PAYMENT SUCCESSFUL[/bold green]",
            border_style="green"
        )
    )

    table = Table(title="Payment Receipt")

    table.add_column("Field", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Payment ID", payment_id)
    table.add_row("Booking ID", booking_id)
    table.add_row("Movie", booking[8])
    table.add_row("Theatre", booking[9])
    table.add_row("Seats", booking[3])
    table.add_row("Amount", "₹" + str(amount))
    table.add_row("Payment Method", payment_method)
    table.add_row("Payment Status", payment_status)

    console.print(table)

    print("\nReceipt Saved At :", pdf_path)

    conn.close()