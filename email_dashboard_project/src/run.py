from email_smtplib import schedule_email
from db import get_scheduled_emails

emails = get_scheduled_emails()


for email in emails:
    schedule_email(email['to_email'], email['subject'], email['body'], email['scheduled_date'], email['scheduled_time'])