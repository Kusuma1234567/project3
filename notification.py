import smtplib
from email.mime.text import MIMEText
import streamlit as st
EMAIL = st.secrets["EMAIL"]
PASSWORD = st.secrets["PASSWORD"]


# 🔹 Existing function (request status email)
def send_email(receiver_email, name, priority):
    subject = "Certificate Status Update"

    body = f"""
Hi {name},

Your certificate request is received.

Priority: {priority}
Status: Processing

Thank you.
"""

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = receiver_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    server.sendmail(EMAIL, receiver_email, msg.as_string())
    server.quit()


# 🔥 NEW FUNCTION (ADMIN REPLY EMAIL)
def send_reply_email(receiver_email, name, reply):
    subject = "Certificate Request Reply"

    body = f"""
Hi {name},

Admin has replied to your certificate request:

Reply:
{reply}

Thank you.
"""

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = receiver_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    server.sendmail(EMAIL, receiver_email, msg.as_string())
    server.quit()
