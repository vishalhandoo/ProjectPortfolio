import smtplib as smtp
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "vishalhandoo067@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "vishalhandoo067@gmail.com"
    context = ssl.create_default_context()

    with smtp.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


