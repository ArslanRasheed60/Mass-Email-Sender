from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import decode_header
import smtplib
from decouple import config
import logging


smtp_server = config("SMTP_SERVER")
smtp_port = config("SMTP_PORT")
smtp_username = config("SMTP_USERNAME")
smtp_password = config("SMTP_PASSWORD")

#logging
logging.basicConfig(
    level=logging.INFO,  # Set the log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def decode_subject(header_value):
    decoded, encoding = decode_header(header_value)[0]
    if encoding is not None:
        return decoded.decode(encoding)
    else:
        return decoded

def send_email(subject, content, recipient):
    try:
        # Create an SMTP client
        smtp = smtplib.SMTP_SSL(smtp_server, smtp_port)
        smtp.login(smtp_username, smtp_password)

        # Create the email message
        msg = MIMEMultipart()
        msg["From"] = smtp_username
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(content, "plain"))

        # Send the email
        smtp.sendmail(smtp_username, recipient, msg.as_string())

        # Close the SMTP connection
        smtp.quit()

        print("Email sent successfully to ", recipient)
        logging.info("Email sent successfully to: ")
        logging.info(recipient)

    except Exception as e:
        print("Error sending email:", str(e))
