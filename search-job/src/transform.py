import pandas as pd
from loguru import logger


def transform(df):

    df['date'] = pd.to_datetime(df['date'])
    print('date type is changed to datetime!')

    BASE_URL = 'https://www.gulftalent.com'
    df['job_link'] = df['job_link'].apply(lambda link: BASE_URL + link)
    logger.info('Base url is added to job link!')

    df['job_link'] = df['job_link'].str.replace('/mobile', '')
    logger.info('job link is modified!')

    return df

def main():
    df = pd.read_csv('src/data/arab_job_search.csv')
    logger.info('dataframe is read from data directory')
    df = transform(df)
    df.to_csv( 'src/data/arab_job_search_transformed.csv', index=False)
    logger.info(f'transformed dataframe is created with shape: {df.info()}')

if __name__ == "__main__":
    main()