import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_HOST = 'localhost'
SMTP_PORT = 1025
FROM_EMAIL = 'admin@mad2.com'

def send_email(to, subject, html_body):
    msg = MIMEMultipart('alternative')

    msg['Subject'] = subject
    msg['From'] = FROM_EMAIL
    msg['To'] = to

    # Attach HTML body
    msg.attach(MIMEText(html_body, 'html'))

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.sendmail(FROM_EMAIL, [to], msg.as_string())

if __name__ == '__main__':
    html = """
    <html>
        <body>
            <h1>Welcome!</h1>
            <p>This is an <b>HTML</b> email.</p>
            <p style="color:blue;">Thanks for registering.</p>
        </body>
    </html>
    """

    send_email(
        "user@example.com",
        "Welcome to MAD2",
        html
    )