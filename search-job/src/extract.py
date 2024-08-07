import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
import tqdm
import datetime
from loguru import logger



def extract_data(url):

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    # soup.find_all('a')

    # Job
    job_title = [element.text.strip() for element in soup.find_all(class_='title')]

    # Location
    location = [element.text for element in soup.find_all(class_="location")]

    # Date
    date = [element.text.strip() for element in soup.find_all(class_="date pull-right")]

    # Company
    company_name = [element.text for element in soup.find_all(class_="company-name")]

    # Link
    link = [a['href'] for a in soup.find_all(class_='ga-job-impression ga-job-click job-results-item section')]

    df = pd.DataFrame({
        'job_title': job_title,
        'location': location,
        'date': date,
        'comany_name': company_name,
        'job_link': link
    }
        )

    logger.info(f"dataframe is created and its shape is: {df.shape}")

    return df

def save_df(df, file_path):

    df.to_csv(file_path, index=False)
    logger.info('dataframe is saved!')


def main():
    URL = 'https://www.gulftalent.com/jobs/search?pos_ref=data&frmPositionCountry=#!?category=&industry=&seniority=&country=&city=&employment_type=&has_external_application=&keyword=data'
    df = extract_data(URL)
    save_df(df, 'src/data/arab_job_search.csv')

if __name__ == '__main__':
    main()

