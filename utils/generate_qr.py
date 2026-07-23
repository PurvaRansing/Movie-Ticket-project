import qrcode
import os

def generate_qr(booking_id, payment_id, movie_name, seats, amount):

    data = f"""
Movie Ticket

Booking ID : {booking_id}
Payment ID : {payment_id}
Movie : {movie_name}
Seats : {seats}
Amount : ₹{amount}
"""

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )

    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")

    if not os.path.exists("qr_codes"):
        os.makedirs("qr_codes")

    file_path = f"qr_codes/{booking_id}.png"

    image.save(file_path)

    return file_path