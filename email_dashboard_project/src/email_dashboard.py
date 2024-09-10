import datetime
import os

import streamlit as st

from db import ingest_data



st.title("Sending and Scheduling :blue[Emails] :sunglasses:")



col1, col2, col3 = st.columns(3)

with col1:
    to_email = st.text_input("Recipient Email", " ")
    

with col2:
    subject = st.text_input("Subject", " ")
    body = st.text_input("Message Body", " ")
    

with col3:
       
    scheduled_date = st.date_input("Scheduled Date", value=datetime.date.today())
    scheduled_time = st.time_input("Scheduled Time") #value=datetime.datetime.now())
    
    


scheduled_email_button = st.button("Scheduled Email")
if scheduled_email_button:
    
     # Indest data to database  
    ingest_data(to_email, subject, body, scheduled_date, scheduled_time)

    st.success('Email Scheduling Successful')
    

    
     

    
   