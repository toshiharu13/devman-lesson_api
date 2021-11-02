import requests
import os
from dotenv import load_dotenv
load_dotenv()

def shorten_link(token, url, link_to_bitly):
    body = {"long_url": link_to_bitly}
    headers = {'Authorization': token}
    check_for_correct_link = requests.get(link_to_bitly)
    check_for_correct_link.raise_for_status()
    response = requests.post(url, headers=headers, json=body)
    return response.json()['link']


url = 'https://api-ssl.bitly.com/v4/bitlinks'
key = os.getenv('KEY')
link_to_bitly = input('Веедите адрес для битлинка: ')

print(f'Битлинк: {shorten_link(key, url, link_to_bitly)}')

