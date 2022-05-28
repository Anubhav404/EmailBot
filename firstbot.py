
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

# Connection with the server
server = smtplib.SMTP(anubhavsoni456@gmail.com  , 578)
server.starttls()
server.login(anubhavsoni456@gmai.com    , 1@Anuhbav)

# Creation of the MIMEMultipart Object
message = MIMEMultipart()

# Setup of MIMEMultipart Object Header
message['From'] = "anubhavsoni456@gmail.com"
message['To'] = "aringoyal.cse24@jecrc.ac.in"
message['Subject'] = "Automated Email with Attachment For The First Time"

# Creation of a MIMEText Part
textPart = MIMEText("This is my first plain text automated Email with an Attachment.\n\nAlessio", 'plain')

# Creation of a MIMEApplication Part
filename = "document.txt"
filePart = MIMEApplication(open(filename,"rb").read(),Name=filename)
filePart["Content-Disposition"] = 'attachment; filename="%s' % filename

# Parts attachment
message.attach(textPart)
message.attach(filePart)

# Send Email and close connection
server.send_message(message)
print(message)
server.quit()