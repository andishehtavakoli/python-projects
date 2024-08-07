from sqlalchemy import create_engine, Column, Integer, String, text, Date
from sqlalchemy.orm import Session, declarative_base

# Create engine
def db_connection(db_name):

    db_info = {
    'username':'andisheh',
    'password': '12345',
    'host': 'localhost',
    'port':'5432',
}

    username = db_info['username']
    password = db_info['password']
    host = db_info['host']
    port = db_info['port']

    # Core Approch for building database
    engine = create_engine(f"postgresql://{username}:{password}@{host}:{port}/{db_name}")

    return engine

def create_new_db(db_info, db_name):

    # create engine
    engine = db_connection('postgres')

    # Create connection
    with engine.connect() as connection:
            connection.execute(text("COMMIT"))
            connection.execute(text(f"DROP DATABASE IF EXISTS {db_name}"))
            connection.execute(text(f"CREATE DATABASE {db_name}"))
            connection.commit()
