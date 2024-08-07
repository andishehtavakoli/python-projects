from sqlalchemy import create_engine, Column, Integer, String, text, Date
from sqlalchemy.orm import Session, declarative_base
from src.utils import db_connection, create_new_db
import pandas as pd
from loguru import logger

DB_NAME = 'arab_search_job'
db_info = {
'username':'andisheh',
'password': '12345',
'host': 'localhost',
'port':'5432',
}

# Connect to new database-----------------------------------------
create_new_db(db_info, DB_NAME)
logger.info(f'{DB_NAME} database is created')

# Create Table with SQLalchemy (ORM)-----------------------------------------
engine = db_connection(DB_NAME)
logger.info('engine is created!')

session = Session(engine)
logger.info('session is created!')

Base = declarative_base()

class ArabJob(Base):

    __tablename__ = 'arabjobsearch'
    id = Column(Integer, primary_key=True)
    job_title = Column(String)
    location = Column(String)
    date = Column(Date)
    comany_name = Column(String)
    job_link = Column(String)


Base.metadata.create_all(engine)
session.commit()
logger.info('table is created!')


# Insert data in arabjobsearch table-----------------------------------------
def main():
    df = pd.read_csv('src/data/arab_job_search_transformed.csv')
    print(df.head())
    list_of_job_row = [ArabJob(**row) for row in df.to_dict(orient='records')]

    session.add_all(list_of_job_row)
    session.commit()
    logger.info('data is inserted in database')

if __name__ == '__main__':
    main()
