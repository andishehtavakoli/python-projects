import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from loguru import logger
import os
from dotenv import load_dotenv
        
import schedule
import time
import datetime


load_dotenv()

# Email configuration
sender_email = os.getenv(key='sender_email')
sender_password = os.getenv(key='sender_password')
    


def send_email(to_email, subject, body):
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    # Attach the body to the email
    msg.attach(MIMEText(body, 'plain'))
    
    # Try to connect to the SMTP server and send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        
        # Send the email
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
        return "Sent"
    except Exception as e:
        print(f"Failed to send email: {e}")
        return f"Failed: {e}"
    

def schedule_email(to_email, subject, body, scheduled_date, scheduled_time):
    status = "Scheduled"  # Initial status when the email is scheduled
    
    # Combine scheduled date and time into a datetime object
    scheduled_datetime_str = f"{scheduled_date} {scheduled_time}"
    try:
        scheduled_datetime = datetime.datetime.strptime(scheduled_datetime_str, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return "Failed: Invalid date or time format."
    
    # Calculate the time difference from now until the scheduled time
    now = datetime.datetime.now()
    if scheduled_datetime < now:
        return "Failed: Scheduled time is in the past."
    
    # Define the job to be scheduled
    def job():
        nonlocal status
        status = send_email(to_email, subject, body)
    
    # Schedule the job at the exact time
    schedule_time = scheduled_datetime.strftime('%H:%M:%S')
    schedule.every().day.at(schedule_time).do(job)
    
    print(f"Email scheduled to be sent at {scheduled_time} on {scheduled_date}.")
    
    # Run the schedule continuously in the background
    while True:
        schedule.run_pending()
        time.sleep(1)
    
    return status


#