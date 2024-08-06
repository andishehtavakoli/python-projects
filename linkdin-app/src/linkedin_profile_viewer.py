import os
from pathlib import Path

import requests
from dotenv import load_dotenv

from utils import save_file

DATA_DIR = Path('.').resolve()
print(DATA_DIR )
ENV_PATH = DATA_DIR / '.env'
print(ENV_PATH )
load_dotenv(dotenv_path=ENV_PATH)
RAPIDAPI_KEY = os.getenv('x_rapidapi_key')


def get_linkedin_profile(username):
    url = "https://linkedin-data-api.p.rapidapi.com/"
    # x_rapidapi_key =  RAPIDAPI_KEY

    querystring = {"username": username}

    headers = {
    	"x-rapidapi-key": RAPIDAPI_KEY,
    	"x-rapidapi-host": "linkedin-data-api.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    
    return response.text


if __name__ == '__main__':
    profile_data = get_linkedin_profile('sinanazem')
    print(profile_data)
    