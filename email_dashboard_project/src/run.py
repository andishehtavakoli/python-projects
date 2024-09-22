from datetime import datetime, timedelta
import time
import threading
from loguru import logger
import pytz

from src.db import get_future_emails, session, EmailSchedule  # Import session and EmailSchedule to update statuses
from src.email_smtplib import send_email

# Assuming your project needs the Iran Standard Time zone.
IRAN_TZ = pytz.timezone('Asia/Tehran')

def check_and_send_emails():
    """Check the database for future emails and send them if it's time."""
    future_emails = get_future_emails()
    
    if not future_emails:
        logger.info("No emails to schedule.")
        return None
    
    now = datetime.now(IRAN_TZ).replace(second=0, microsecond=0)  # Strip seconds and microseconds and ensure correct time zone
    closest_email_time = None
    
    for email in future_emails:
        # Combine scheduled date and time into a single datetime object, ignoring seconds
        scheduled_datetime = datetime.combine(email['scheduled_date'], email['scheduled_time']).replace(second=0, microsecond=0)
        scheduled_datetime = IRAN_TZ.localize(scheduled_datetime)  # Localize to Iran Standard Time

        logger.info(f'Time now is: {now} and Scheduled Time is: {scheduled_datetime}')
        
        # Check if it's time to send the email (ignoring seconds) and the email is pending or failed
        if scheduled_datetime <= now and email['status'] in ['pending', 'failed']:
            try:
                logger.info(f"Sending email to {email['to_email']}")
                send_email(email['to_email'], email['subject'], email['body'])
                
                # Update status to 'sent' after successful send
                update_email_status(email['id'], 'sent')
                logger.info(f"Email sent to {email['to_email']} and status updated to 'sent'")
            except Exception as e:
                # Log the error and update status to 'failed'
                logger.error(f"Failed to send email to {email['to_email']}. Error: {str(e)}")
                update_email_status(email['id'], 'failed')
                logger.info(f"Email status updated to 'failed' for {email['to_email']}")
        else:
            # If the scheduled time is in the future, track the closest future email
            if closest_email_time is None or scheduled_datetime < closest_email_time:
                closest_email_time = scheduled_datetime
                logger.info(f"Next closest email is scheduled for {closest_email_time}")
    
    return closest_email_time


def update_email_status(email_id, new_status):
    """Update the status of an email in the database."""
    email_record = session.query(EmailSchedule).filter(EmailSchedule.id == email_id).first()
    if email_record:
        email_record.status = new_status
        session.commit()


def schedule_dynamic_check():
    """Dynamically schedule checks based on the next email time."""
    while True:
        closest_email_time = check_and_send_emails()
        if closest_email_time:
            now = datetime.now(IRAN_TZ).replace(second=0, microsecond=0)
            sleep_duration = (closest_email_time - now).total_seconds()
            
            # Ensure we don't sleep for a negative or too small interval
            if sleep_duration > 0:
                logger.info(f"Waiting {sleep_duration:.2f} seconds until next email at {closest_email_time}")
                time.sleep(sleep_duration)
            else:
                logger.info(f"Scheduled time {closest_email_time} is in the past, checking again immediately.")
        else:
            logger.info("No future emails found. Checking again in 10 seconds.")
            time.sleep(10)  # Check again after 10 seconds if no future emails


if __name__ == '__main__':
    # Start the dynamic email scheduler
    logger.info("Starting the dynamic email scheduler...")
    schedule_dynamic_check()