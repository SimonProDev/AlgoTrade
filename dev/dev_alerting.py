import os
from dotenv import load_dotenv
import smtplib
import ssl

port = 465  # For SSL

load_dotenv()
email = str(os.getenv('GMAIL_ADDRESS'))
password = str(os.getenv('GMAIL_PW'))
message = """\
Subject: AlgoTrade

This mail is sent from python script
"""

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("simon.barghi.dev@gmail.com",
                 password)
    server.sendmail(email,
                    email,
                    message)
