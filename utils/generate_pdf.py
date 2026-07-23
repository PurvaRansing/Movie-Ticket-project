from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
import os


def generate_pdf(
    booking_id,
    payment_id,
    user_id,
    movie_name,
    theatre_name,
    show_date,
    show_time,
    seats,
    amount,
    payment_method,
    payment_date,
    qr_path
):

    if not os.path.exists("receipts"):
        os.makedirs("receipts")

    pdf_path = f"receipts/{booking_id}.pdf"

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b><font size=18>MOVIE TICKET RECEIPT</font></b>", styles["Title"]))
    story.append(Spacer(1,20))

    story.append(Paragraph(f"<b>Booking ID :</b> {booking_id}", styles["Normal"]))
    story.append(Paragraph(f"<b>Payment ID :</b> {payment_id}", styles["Normal"]))
    story.append(Paragraph(f"<b>User ID :</b> {user_id}", styles["Normal"]))

    story.append(Spacer(1,10))

    story.append(Paragraph(f"<b>Movie :</b> {movie_name}", styles["Normal"]))
    story.append(Paragraph(f"<b>Theatre :</b> {theatre_name}", styles["Normal"]))
    story.append(Paragraph(f"<b>Show Date :</b> {show_date}", styles["Normal"]))
    story.append(Paragraph(f"<b>Show Time :</b> {show_time}", styles["Normal"]))

    story.append(Spacer(1,10))

    story.append(Paragraph(f"<b>Seats :</b> {seats}", styles["Normal"]))
    story.append(Paragraph(f"<b>Amount :</b> ₹{amount}", styles["Normal"]))
    story.append(Paragraph(f"<b>Payment Method :</b> {payment_method}", styles["Normal"]))
    story.append(Paragraph(f"<b>Payment Date :</b> {payment_date}", styles["Normal"]))

    story.append(Spacer(1,20))

    if os.path.exists(qr_path):
        qr = Image(qr_path)
        qr.drawHeight = 150
        qr.drawWidth = 150
        story.append(qr)

    story.append(Spacer(1,20))

    story.append(
        Paragraph(
            "<b>Thank you for booking with CineFlow.</b>",
            styles["Heading2"]
        )
    )

    doc.build(story)

    return pdf_path