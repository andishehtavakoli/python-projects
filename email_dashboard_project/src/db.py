from sqlalchemy import select, Column, Integer, String, Text, DateTime, Enum, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
import enum

# Define the base class for the models
Base = declarative_base()

# Define your model (table)
class People(Base):
    __tablename__ = 'people'  # Table name

    id = Column(Integer, primary_key=True, autoincrement=True)
    sender_email = Column(String(255), nullable=False)
    recipient_email = Column(String(255), nullable=False)
    subject = Column(String(255), nullable=True)
    message_body = Column(Text, nullable=False)
    scheduled_time = Column(DateTime, nullable=False)
    status = Column(String(255), nullable=False)
    
    
    def __repr__(self):
        return f"<Email(id={self.id}, sender={self.sender_email}, recipient={self.recipient_email}, status={self.status})>"
    
    
# Create an engine
engine = create_engine('postgresql://postgres:postgres@localhost/postgres', echo=True)


def ingest_data(sender_email, recipient_email, subject, message_body, scheduled_time, status):
    Session = sessionmaker(bind=engine)
    session = Session()

    new_user = People(
        sender_email=sender_email, 
        recipient_email=recipient_email, 
        subject=subject, 
        message_body=message_body, 
        scheduled_time=scheduled_time, 
        status=status)
    
    session.add(new_user)
    session.commit()
    
    


def get_scheduled_emails():
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        # Query the database for all scheduled emails
        result = session.query(People).all()
        
        # Convert the result into a list of dictionaries
        emails = [{
            'to_email': email.to_email,
            'subject': email.subject,
            'body': email.body,
            'scheduled_date': email.scheduled_date,
            'scheduled_time': email.scheduled_time
        } for email in result]
        
        return emails
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    