import os

import requests
from dotenv import load_dotenv

load_dotenv()


url = 'https://api-ssl.bitly.com/v4/user'
payload = {'Authorization': os.getenv('KEY')}
response = requests.get(url, headers=payload).json()
response.raise_for_status()
print(response)

