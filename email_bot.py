import smtplib, ssl
import getpass
from email.message import EmailMessage
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv("e_variables.env")

MAIL_LIST = os.environ.get("MAIL_LIST", None) # Enter receiver address
SENDER_MAIL = os.environ.get("SENDER_MAIL", None) # Enter your address

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = SENDER_MAIL  
receiver_emails = MAIL_LIST  
password = getpass.getpass()

with open("out_email.html") as html_file:
    soup = BeautifulSoup(html_file, "html.parser")
    file = soup.prettify()

message = EmailMessage()
message["Subject"] = "My daily financial Summary"
message["From"] = sender_email
message["To"] = MAIL_LIST.split(",")

message.add_alternative(file, subtype='html')

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.send_message(message)
    