import requests
import os
from dotenv import load_dotenv
load_dotenv()

def shorten_link(token, url, link_to_bitly):
    body = {"long_url": link_to_bitly}
    headers = {'Authorization': token}
    #check_for_correct_link = requests.get(link_to_bitly)
    #check_for_correct_link.raise_for_status()
    response = requests.post(url, headers=headers, json=body)
    return response.json()['link']


def check_link(link_to_bitly):
    check_for_correct_link = requests.get(link_to_bitly)
    check_for_correct_link.raise_for_status()


url = 'https://api-ssl.bitly.com/v4/bitlinks'
key = os.getenv('KEY')
link_to_bitly = input('Веедите адрес для битлинка: ')
try:
    link = check_link(link_to_bitly)
except requests.exceptions.HTTPError:
    print('не корректная ссылка')

print(f'Битлинк: {shorten_link(key, url, link_to_bitly)}')

