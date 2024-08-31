import streamlit as st
from db import ingest_data
from email_smtplib import send_email, schedule_email
import os
from dotenv import load_dotenv
import datetime




st.title("Sending and Scheduling :blue[Emails] :sunglasses:")

load_dotenv()

# Email configuration
sender_email = os.getenv(key='sender_email')
sender_password = os.getenv(key='sender_password')
    

col1, col2, col3 = st.columns(3)

with col1:
    recipient_mail = st.text_input("Recipient Email", " ")
    

with col2:
    subject = st.text_input("Subject", " ")
    message_body = st.text_input("Message Body", " ")
    

with col3:
    scheduled_date = st.date_input("Scheduled Date", value=datetime.date.today())
    scheduled_time = st.time_input("Scheduled Time") #value=datetime.datetime.now())
    # status = st.text_input("Status", " ")
    


send_email_button = st.button("Send Email")
if send_email_button:

    status = schedule_email(to_email=recipient_mail , subject=subject, body=message_body, scheduled_date=scheduled_date, scheduled_time=scheduled_time)
     # Indest data to database  
    ingest_data(sender_email, recipient_mail, subject, message_body, scheduled_date, status)

    
     

    
   