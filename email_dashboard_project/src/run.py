from datetime import datetime
import time

import schedule
from loguru import logger

from db import get_future_emails
from email_smtplib import send_email


def schedule_emails():
    future_emails = get_future_emails()
    
    if not future_emails:
        logger.info("No emails to schedule.")
        return
    
    for email in future_emails:
        # Combine scheduled date and time into a single datetime object
        scheduled_datetime = datetime.combine(email.scheduled_date, email.scheduled_time)

        # Schedule email if the time is in the future
        now = datetime.now()  # Use datetime from the datetime module
        if scheduled_datetime > now:
            # Define the job to send email
            def job(to=email.to_email, subject=email.subject, body=email.body):
                send_email(to, subject, body)
            
            # Schedule the job at the exact datetime
            time_diff = (scheduled_datetime - now).total_seconds()
            logger.info(f"Scheduling email to {email.to_email} at {scheduled_datetime}")
            schedule.every(time_diff).seconds.do(job)
        else:
            logger.info(f"Skipping email to {email.to_email} because the time has passed.")
            
            
def run_scheduler():
    """Run the scheduler continuously in the background."""
    while True:
        schedule.run_pending()
        time.sleep(1)
        
        
        
if __name__ == '__main__':
    # Schedule emails and start the scheduler
    schedule_emails()
    run_scheduler()










