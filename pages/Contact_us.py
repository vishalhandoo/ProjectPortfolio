import streamlit as st
from send_email import send_email

st.header("Contact Us")

with st.form(key="ContactUsForm"):
    user_email = st.text_input("Your Email Address")
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New Email From {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")

    if button:
        send_email(message)
        st.info("Email was sent successfully")