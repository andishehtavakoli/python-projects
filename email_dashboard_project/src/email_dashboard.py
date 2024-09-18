import datetime
import os
import pandas as pd

import streamlit as st

from src.db import ingest_data, get_emails


st.image('https://tasktak.com/static/media/web-banner.f09d0a107ce1b0f7532c.png', width=300)
st.title("Sending and Scheduling :blue[Emails] :sunglasses:")



col1, col2, col3 = st.columns(3)

with col1:
    to_email = st.text_input("Recipient Email", " ")
    

with col2:
    scheduled_date = st.date_input("Scheduled Date", value=datetime.date.today())


with col3:
       
    
    scheduled_time = st.time_input("Scheduled Time") #value=datetime.datetime.now())
    
subject = st.text_input("Subject", " ")
body = st.text_area("Message Body"," ",)       


scheduled_email_button = st.button("Scheduled Email")
if scheduled_email_button:
    
     # Indest data to database  
    ingest_data(to_email, subject, body, scheduled_date, scheduled_time, status='pending')

    st.success('Email Scheduling Successful')
    
    
 
st.markdown("### Scheduled :blue[Emails]") 

# Function to highlight the categorical column (e.g., column 'A')
def highlight_column_with_style(column_name):
    def highlight(s):
        return ['background-color: yellow; color: black' if s.name == column_name else '' for _ in s]
    return highlight

email_df = pd.DataFrame(get_emails())
email_df.drop(columns=['body', 'id'], inplace=True)

# Applying the style to the DataFrame
styled_email_df = email_df.style.apply(highlight_column_with_style('status'), axis=0)
st.dataframe(styled_email_df)  

    
     

    
   