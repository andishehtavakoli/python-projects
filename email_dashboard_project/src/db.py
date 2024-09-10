import datetime
import time

import schedule
from sqlalchemy import Column, Date, Integer, String, Time, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define your SQLAlchemy base and model
Base = declarative_base()


# Email schedule table model (replace with your actual table schema)
class EmailSchedule(Base):
    __tablename__ = 'email_schedule'
    id = Column(Integer, primary_key=True)
    to_email = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    body = Column(String, nullable=False)
    scheduled_date = Column(Date, nullable=False)
    scheduled_time = Column(Time, nullable=False)

# Database connection setup (PostgreSQL)
DATABASE_URL = "postgresql://postgres:postgres@localhost/postgres"
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Create the email_schedule table in the database
Base.metadata.create_all(engine)


def ingest_data(to_email, subject, body, scheduled_date, scheduled_time):
    new_user = EmailSchedule(
        to_email=to_email, 
        subject=subject, 
        body=body,
        scheduled_date=scheduled_date, 
        scheduled_time=scheduled_time, 
       )
    
    session.add(new_user)
    session.commit()
    
    
def get_future_emails():
    # Get the current date and time
    now = datetime.datetime.now()

    # Query the database for all emails scheduled in the future
    future_emails = session.query(EmailSchedule).filter(
        (EmailSchedule.scheduled_date + EmailSchedule.scheduled_time) > now
    ).all()

    # Check if there are any future emails
    if future_emails:
        # Create a list of dictionaries with email data
        email_list = [
            {
                "id": email.id,
                "to_email": email.to_email,
                "subject": email.subject,
                "body": email.body,
                "scheduled_date": email.scheduled_date,
                "scheduled_time": email.scheduled_time
            }
            for email in future_emails
        ]
        return email_list
    else:
        return []
    
    



