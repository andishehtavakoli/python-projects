import pandas as pd
import numpy as np
import missingno as msno
from loguru import logger
import sqlalchemy
from sqlalchemy import create_engine

# read data
def extract_data(file_path):
    logger.info('getting data')
    df = pd.read_csv(file_path)
    logger.info('data is extracted')
    return df

file_path = 'src/data/AB_NYC_2019.csv'
airbnb_df = extract_data(file_path)

# clean data
def transform_data(df):
    logger.info(f'shape of data is:{df.shape}')

    # remove na for last_review
    df['last_review'] = pd.to_datetime(df['last_review'])
    df['last_review'] = df['last_review'].fillna(df['last_review'].max())
    logger.info(f'removed na from last_review column')

    # remove na for reviews_per_month
    df['reviews_per_month'] = df['reviews_per_month'].fillna(0)
    logger.info(f'removed na from reviews_per_month column')

    # drop columns
    df = df.drop(columns=['name', 'host_name'])
    logger.info(f'removed columns name and host_name')

    return df.head()

clean_data = transform_data(airbnb_df)

# load data
def load_data():
    engine = create_engine('postgresql://andisheh:12345@localhost:5432/airbnb_data')
    clean_data .to_sql('airbnb_newyork', engine)
    logger.info('data is loaded in database')

if __name__ == '__main__':

    load_data()