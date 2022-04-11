import smtplib, ssl
import getpass
from email.message import EmailMessage
from bs4 import BeautifulSoup

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "druginteractionbot@gmail.com"  # Enter your address
receiver_email = "efmontecinos@uc.cl"  # Enter receiver address
password = getpass.getpass()

message = EmailMessage()
message["Subject"] = "test"
message["From"] = sender_email
message["To"] = receiver_email

with open("out_email.html") as html_file:
    soup = BeautifulSoup(html_file, "html.parser")
    file = soup.prettify()

message.add_alternative(file, subtype='html')

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.send_message(message)
    