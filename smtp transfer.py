#!/usr/lib/python
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

emailfrom = "valentin.mihai@vodafone.com"
emailto = ["valentin.mihai@vodafone.com", "mihai_valentin100@yahoo.com"]
server_addr = "10.50.169.99"
# fileToSend = "example.txt"
fileToSend = "1.PNG"
def send_email(emailfrom,emailto,server_addr):


    msg = MIMEMultipart()
    msg["From"] = emailfrom
    msg["To"] = ",".join(emailto)
    msg["Subject"] = "YOUR EMAIL SUBJECT"
    msg.preamble = "YOUR EMAIL SUBJECT"

    ctype, encoding = mimetypes.guess_type(fileToSend)
    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"

    maintype, subtype = ctype.split("/", 1)

    fp = open(fileToSend, "rb")
    attachment = MIMEBase(maintype, subtype)
    attachment.set_payload(fp.read())
    fp.close()
    encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
    msg.attach(attachment)

    server = smtplib.SMTP(server_addr)
    #server.set_debuglevel(0)
    server.sendmail(emailfrom, emailto, msg.as_string())
    server.quit()

send_email(emailfrom,emailto,server_addr)