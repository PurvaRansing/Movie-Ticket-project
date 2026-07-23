import yagmail
from utils.config import EMAIL, APP_PASSWORD


def send_email(receiver_email, pdf_path):

    try:

        yag = yagmail.SMTP(
            user=EMAIL,
            password=APP_PASSWORD
        )

        subject = "Movie Ticket Receipt"

        body = """
Hello,

Your movie ticket has been booked successfully.

Please find the attached ticket receipt.

Thank you for using CineFlow Movie Booking System.

Enjoy your movie!
"""

        yag.send(
            to=receiver_email,
            subject=subject,
            contents=body,
            attachments=pdf_path
        )

        print("\nEmail Sent Successfully.")

    except Exception as e:

        print("\nEmail Sending Failed.")
        print(e)